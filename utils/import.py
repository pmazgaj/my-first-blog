"""
File for importing csv directly into models.
Currently - for shop and category models.
"""
import csv
import os

from definitions import csv_dir


def parse_shop(filename):
    """
    parse information from shop file, 
    if key not found - set default
    """
    # django.setup()

    path = os.path.join(csv_dir, filename)

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
    # return shop


def parse_category(filename):
    """
    parse information for category
    """
    # django.setup()

    path = os.path.join(csv_dir, filename)

    reader = csv.DictReader(open(path))
    for row in reader:
        category = Category()
        category.id = row.get('id', 0)
        category.name = row.get('name', '--name--')
        category.visible = row.get('visible', True)
        category.save()
    # return category


parse_shop(filename="shops.csv")
parse_shop(filename="categories.csv")
