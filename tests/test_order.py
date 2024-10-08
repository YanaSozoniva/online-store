import pytest

from src.exception import ZeroQuantityProduct
from src.order import Order


def test_order_init(order1, order2):
    """Тестирования инициализации объекта класса Заказ"""
    assert order1.quantity == 2
    assert order1.total_cost == 420000
    assert order1.product.name == "Iphone 15"

    assert order2.product.description == "1024GB, Синий"
    assert order2.quantity == 14


def test_order_str(order1):
    """Тестирование магического метода str класса Заказ"""
    assert str(order1) == "Заказ товара Iphone 15, количество заказанного товара: 2 шт. Сумма заказа 420000"


def test_custom_exception_product_order(capsys, product_2):
    """Тестирование добавления товара с нулевым количеством"""
    with pytest.raises(ZeroQuantityProduct):
        Order(product_2, 0)
        message = capsys.readouterr()
        assert message.out.strip().split("\n")[-2] == "Нельзя заказать товар с нулевым количеством"
        assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"


def test_add_product_order_success(capsys, product_2):
    """Тестирование добавления товара с нулевым количеством"""
    Order(product_2, 2)

    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"
