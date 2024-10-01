import pytest


def test_lawn_grass_init(grass1):
    """Тестирование корректности инициализации объектов класса LawnGrass"""
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.color == "Зеленый"
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"


def test_lawn_grass_add(grass1, grass2):
    """Тестирование сложения 2-х объектов класса LawnGrass"""
    assert grass1 + grass2 == 16750


def test_lawn_grass_add_error(grass1):
    """Тестирование возникновения ошибки при сложении объекта класса LawnGrass и объекта другого класса"""
    with pytest.raises(TypeError):
        result = 1 + grass1
