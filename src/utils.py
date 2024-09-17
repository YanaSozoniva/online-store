import os
import json

from src.product import Product
from src.category import Category


def read_json(path_file: str) -> dict | str:
    """Функция считывает данные из json-файла"""
    if not os.path.exists(path_file):
        return "Файл не найден"

    full_path = os.path.abspath(path_file)

    with open(full_path, 'r', encoding='UTF-8') as json_file:
        data_product = json.load(json_file)

    return data_product


def create_objects_json(data: dict):
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products

        categories.append(Category(**category))

    return categories


# if __name__ == '__main__':
#     new_product_data = read_json('../data/products.json')
#     print(new_product_data)
#     product_data = create_objects_json(new_product_data)
#     print(product_data)
#
#     print(product_data[0].name)
#     print(product_data[0].products)