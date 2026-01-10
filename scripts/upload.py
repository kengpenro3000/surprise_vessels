
from sv_main.models import Category, Item
from django.conf import settings as django_settings

import os
import json
import zipfile
import shutil
import tempfile
import argparse
import sys

# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'surprise.settings')
# django.setup()

os.chdir('../' + os.getcwd())
# print(os.getcwd())


MEDIA_ROOT = django_settings.MEDIA_ROOT

parser = argparse.ArgumentParser(
    description='Upload categories and items from JSON files and zip archives')
parser.add_argument('--categories-json', type=str,
                    help='Path to categories JSON file')
parser.add_argument('--items-json', type=str, help='Path to items JSON file')
parser.add_argument('--categories-zip', type=str,
                    help='Path to zip file containing category images')
parser.add_argument('--items-zip', type=str,
                    help='Path to zip file containing vessel images')
args = parser.parse_args()

categories_json_path = args.categories_json
items_json_path = args.items_json
categories_zip_path = args.categories_zip
items_zip_path = args.items_zip

# 1. extract file paths from user data
paths = [categories_json_path, items_json_path,
         categories_zip_path, items_zip_path]
for path in paths:
    if path:
        sys.stderr.write(f"Invalid path: {path}\n")
        sys.exit(1)

# 2. read categories
if categories_json_path:
    if not categories_json_path.strip():
        sys.stderr.write("Categories JSON path is empty\n")
        sys.exit(1)

    try:
        with open(categories_json_path, 'r') as f:
            categories_data = json.load(f)
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Corrupted categories JSON: {e}\n")
        sys.exit(1)

    if categories_zip_path:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(categories_zip_path, 'r') as zip_temp:
                zip_temp.extractall(temp_dir)

            all_files = []
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    all_files.append(file)
            if len(all_files) != len(set(all_files)):
                sys.stderr.write(
                    "Duplicate filenames in categories zip file\n")
                sys.exit(1)

            items_cats_dir = os.path.join(temp_dir, 'items_cats')
            if os.path.exists(items_cats_dir):
                shutil.move(items_cats_dir, os.path.join(
                    MEDIA_ROOT, 'items_cats'))

    categories_to_create = []
    for item in categories_data:
        name = item.get('name')
        if Category.objects.filter(name=name).exists():
            print(f"Duplicate Category: {name} \n Want to continue? (y/n)")
            answer = input().strip().lower()
            if answer != 'y':
                continue
            else:
                sys.exit(1)

        cat = Category(
            name=name,
            description=item.get('description', ''),
            parameters=item.get('parameters', {"a": 0, "b": 0, "c": 0}),
            rating=item.get('rating', 0)
        )

        image_filename = item.get('image')
        if image_filename:
            cat.image = f"items_cats/{image_filename}"
        categories_to_create.append(cat)

    Category.objects.bulk_create(categories_to_create)


if items_json_path:
    if not items_json_path.strip():
        sys.stderr.write("Items JSON path is empty\n")
        sys.exit(1)

    try:
        with open(items_json_path, 'r') as f:
            items_data = json.load(f)
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Corrupted items JSON: {e}\n")
        sys.exit(1)

    if items_zip_path:
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(items_zip_path, 'r') as zip_dir:
                zip_dir.extractall(temp_dir)

            all_files = []
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    all_files.append(file)
            if len(all_files) != len(set(all_files)):
                sys.stderr.write("Duplicate filenames in items zip file\n")

            items = os.path.join(temp_dir, 'items')
            if os.path.exists(items_dir):
                shutil.move(items_dir, os.path.join(MEDIA_ROOT, 'items'))

    items_to_create = []
    for item in items_data:
        category_name = item.get('category')
        try:
            cat = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            sys.stderr.write(
                f"No Category found for item: {item.get('name')}, category: {category_name}\n")
            sys.exit(1)

        name = item.get('name')
        itm = Item(
            name=name,
            description=item.get('description', ''),
            category=cat
        )
        image_filename = item.get('image')
        if image_filename:
            itm.image = f"items/{image_filename}"
        items_to_create.append(itm)

    Item.objects.bulk_create(items_to_create)
