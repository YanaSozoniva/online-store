from unittest.mock import patch

import pytest

from src.product import Product


def test_product(product_1):
    """Тестирование корректности инициализации объектов класса Product"""
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 23100
    assert product_1.quantity == 5


def test_new_product():
    """Тестирование добавления нового продукта из переданного словаря"""
    new_product = Product.new_product(
        {
            "name": "Samsung S27 Ultra",
            "description": "256GB, Розовый цвет, 400MP камера",
            "price": 480000.0,
            "quantity": 2,
        }
    )

    assert new_product.name == "Samsung S27 Ultra"
    assert new_product.price == 480000.0
    assert new_product.description == "256GB, Розовый цвет, 400MP камера"
    assert new_product.quantity == 2


def test_new_product_and_list_products(category_1):
    """Тестирование корректного добавления нового товара, с учетом проверки такого же товара"""
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23",
            "description": "256GB, Розовый цвет, 400MP камера",
            "price": 72000.0,
            "quantity": 3,
        },
        category_1.products_in_list,
    )

    assert new_product.name == "Samsung Galaxy S23"
    assert new_product.price == 180000.0
    assert new_product.quantity == 8


def test_price_property(product_1):
    """Тестирование геттера price"""
    assert product_1.price == 23100


def test_price_setter(capsys, product_1):
    """Тестирование сеттера price"""
    product_1.price = 250000
    assert product_1.price == 250000

    product_1.price = -123
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    assert product_1.price == 250000


def test_price_setter_price_is_lower_answer_yes(product_1):
    """Тестирование сеттера price, если цена ниже предыдущей"""

    with patch("src.product.input", return_value="y"):
        product_1.price = 2500

    assert product_1.price == 2500


def test_price_setter_price_is_lower_answer_no(product_1):
    """Тестирование сеттера price, если цена ниже предыдущей"""

    with patch("src.product.input", return_value="n"):
        product_1.price = 2500

    assert product_1.price == 23100


def test_product_str(product_1):
    """Тестирование магического метода str класса Product"""
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 23100 руб. Остаток: 5 шт."


def test_products_add(product_1, product_2):
    """Тестирование суммы произведений цены на количество у двух объектов класса Product"""
    assert product_1 + product_2 == 1165500


def test_zero_quantity_add_product():
    """Тестирование возбуждения ошибки при попытке добавить товар с нулевым количеством"""
    with pytest.raises(ValueError):
        Product(
            name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=23100, quantity=0
        )
