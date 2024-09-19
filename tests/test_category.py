def test_category(category_1, category_2):
    """Тестирование корректности инициализации объектов класса Category"""
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных" " функций для удобства жизни"
    )
    assert len(category_1.products) == 3

    assert category_1.count_categories == 2
    assert category_1.count_products == 4

    assert category_2.count_categories == 2
    assert category_2.count_products == 4
