from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('--categories-json', type=str,
                    help='Path to categories JSON file')
        parser.add_argument('--items-json', type=str, help='Path to items JSON file')
        parser.add_argument('--categories-zip', type=str,
                        help='Path to zip file containing category images')
        parser.add_argument('--items-zip', type=str,
                        help='Path to zip file containing vessel images')

    def handle(self, *args, **options):

        categories_json = options['categories-json']

