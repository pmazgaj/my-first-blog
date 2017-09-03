"""
Parse given csv files, to proper format.
"""
import csv

__author__ = "Przemek"


def parse_shop():
    path = "C:/IMS_ZADANIE/Zadanie/Pliki/shops.csv"
    """
    parse information from shop file
    """
    reader = csv.DictReader(open(path))
    shops_list = []
    for row in reader:
        shops_list.append(row)
    return shops_list


def parse_category():
    path = "C:/IMS_ZADANIE/Zadanie/Pliki/categories.csv"
    """
    parse information for category
    """
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


# parse_category()
parse_shop()
