Test JSON files for `scripts/upload.py`

Files added/updated:

- `test_cats.json` — valid sample categories (2 entries)
- `test_items.json` — valid sample items (2 entries)
- `test_cats_invalid.json` — invalid categories (missing name, duplicate)
- `test_items_invalid.json` — invalid items (orphan category, missing fields)
- `test_cats_bulk.json` — bulk categories (5 entries)
- `test_items_bulk.json` — bulk items (20 entries)

How to run the upload script with these samples:

```
python3 scripts/upload.py --categories-json scripts/test_cats.json --items-json scripts/test_items.json

# Bulk import
python3 scripts/upload.py --categories-json scripts/test_cats_bulk.json --items-json scripts/test_items_bulk.json

# Test invalid cases (expect errors or stderr messages)
python3 scripts/upload.py --categories-json scripts/test_cats_invalid.json --items-json scripts/test_items_invalid.json
```

Notes:
- The script expects image files (if provided in JSON) to be located inside zip archives that, when extracted, contain `items/` and/or `items_cats/` directories. Pass those zips via `--items-zip` and `--categories-zip`.
- If you want to test zip handling, create a zip containing `items/` and `items_cats/` with the corresponding image filenames used above.
