def test_product(product_1):
    """Тестирование корректности инициализации объектов класса Product"""
    assert product_1.name == 'Samsung Galaxy S23 Ultra'
    assert product_1.description == '256GB, Серый цвет, 200MP камера'
    assert product_1.price == 23100
    assert product_1.quantity == 5
