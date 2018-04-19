"""
Parse given csv files, to proper format.
"""
import csv
import os

from constants import CSV_FILE_PATH

__author__ = "Przemek"


class CsvParsers:
    @staticmethod
    def parse_shop():
        """
        parse information from shop file
        """
        path = os.path.join(CSV_FILE_PATH, 'categories.csv')
        reader = csv.DictReader(open(path))
        shops_list = []
        for row in reader:
            shops_list.append(row)
        return shops_list

    @staticmethod
    def parse_category():
        """
        parse information for category
        """
        path = os.path.join(CSV_FILE_PATH, 'categories.csv')
        id_list = []
        visible_list = []
        name_list = []
        categories = []
        reader = csv.DictReader(open(path))
        for row in reader:
            id_list.append(row.get('id', 0))
            visible_list.append(row.get('visible', False))
            name_list.append(row.get('name', '--name--'))
            categories.append(row)

        return categories


if __name__ == '__main__':
    csv_parser = CsvParsers()
    # parse_category()
    csv_parser.parse_shop()
