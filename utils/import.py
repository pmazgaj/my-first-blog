"""
File for importing csv directly into models.
Currently - for shop and category models.
"""
import csv
import django
import os

from shop.models import Shop
from utils.parse_csv import CsvParsers

django.setup()


class FillModelsFromCsvData:
    def __init__(self):
        django.setup()
        self.csv_parser = CsvParsers()

    def import_shop_data(self):
        """
        parse information from shop file,
        if key not found - set default
        """
        reader = self.csv_parser.parse_shop()
        for row in reader:
            shop = Shop()
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

    def import_category_data(self):
        """
        parse information for category
        """
        reader = self.csv_parser.parse_category()

        for row in reader:
            category = Category()
            category.id = row.get('id', 0)
            category.name = row.get('name', '--name--')
            category.visible = row.get('visible', True)
            category.save()
        # return category


if __name__ == '__main__':
    model_filler = FillModelsFromCsvData()
    model_filler.import_shop_data(filename="shops.csv")
    model_filler.import_category_data(filename="categories.csv")
