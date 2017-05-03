"""
File for importing csv directly into models.
Currently - for shop and category models.
"""
import csv
import sys
import os
import django
from shop.models import Shop
from shop.models import Category


__author__ = "Przemek"

project_dir = "C:/IMS_ZADANIE/ims/ims_site/ims_site"

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

django.setup()


def parse_shop(path):
    """
    parse information from shop file, 
    if key not found - set default
    """
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

    reader = csv.DictReader(open(path))
    for row in reader:
        category = Category()
        category.id = row.get('id', 0)
        category.name = row.get('name', '--name--')
        category.visible = row.get('visible', True)
        category.save()

parse_category("C:/IMS_ZADANIE/ims/ims_site/categories.csv")
# parse_shop("C:/IMS_ZADANIE/ims/ims_site/shops.csv")
