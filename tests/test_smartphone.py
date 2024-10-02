import pytest


def test_smartphone_init(smartphone1):
    """Тестирование корректности инициализации объектов класса Smartphone"""
    assert smartphone1.name == "Xiaomi Redmi Note 11"
    assert smartphone1.description == "1024GB, Синий"
    assert smartphone1.price == 31000.0
    assert smartphone1.efficiency == 90.3
    assert smartphone1.quantity == 14
    assert smartphone1.color == "Синий"
    assert smartphone1.model == "Note 11"
    assert smartphone1.memory == 1024


def test_smartphone_add(smartphone1, smartphone2):
    """Тестирование сложения 2-х объектов класса Smartphone"""
    assert smartphone1 + smartphone2 == 2114000


def test_smartphone_add_error(smartphone1, grass1):
    """Тестирование возникновения ошибки при сложении объекта класса Smartphone и объекта другого класса"""
    with pytest.raises(TypeError):
        result = smartphone1 + grass1
