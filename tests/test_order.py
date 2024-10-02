def test_order_init(order1, order2):
    """Тестирования инициализации объекта класса Заказ"""
    assert order1.quantity == 2
    assert order1.total_cost == 420000
    assert order1.product.name == 'Iphone 15'

    assert order2.product.description == "1024GB, Синий"
    assert order2.quantity == 14


def test_order_str(order1):
    """Тестирование магического метода str класса Заказ"""
    assert str(order1) == "Заказ товара Iphone 15, количество заказанного товара: 2 шт. Сумма заказа 420000"
