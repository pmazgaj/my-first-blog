"""
File for importing csv directly into models.
Currently - for shop and category models.
"""
import csv
import sys
import os
import django
import logging
from paths import IMS_PROJECT_PATH, PROJECT_PATH, CSV_PATH
__author__ = "Przemek"

sys.path.append(IMS_PROJECT_PATH)
sys.path.append(PROJECT_PATH)
print(IMS_PROJECT_PATH)
print(PROJECT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def parse_shop(path):
    """
    parse information from shop file, 
    if key not found - set default
    """
    django.setup()

    reader = csv.DictReader(open(path))
    for row in reader:
        shop = Shop()
        # shop.id = row.get('category_id', 0)
        shop.name = row.get('name', '--default--')
        shop.description = row.get('description', '--default--')
        shop.main_category = row.get('category_id', '--default--')
        shop.categories = row.get('category_id', '--default--')
        shop.shop_level = row.get('level', '--default--')
        shop.is_in_lottery = row.get('lottery', '--default--')
        shop.date_of_creation = row.get('created_at', '--default--')
        shop.date_of_update = row.get('updated_at', '--default--')
        shop.save()


def parse_category(path):
    """
    parse information for category
    """
    django.setup()

    reader = csv.DictReader(open(path))
    for row in reader:
        category = md.Category()
        category.id = row.get('id', 0)
        category.name = row.get('name', '--name--')
        category.visible = row.get('visible', True)
        category.save()


parse_category(os.path.join(CSV_PATH, 'categories.csv'))
parse_shop(os.path.join(CSV_PATH, 'shops.csv'))
