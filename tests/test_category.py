import pytest
from src.category import Category


def test_category(category_1, category_2):
    """Тестирование корректности инициализации объектов класса Category"""
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.products_in_list) == 3

    assert category_1.count_categories == 2
    assert category_1.count_products == 4

    assert category_2.count_categories == 2
    assert category_2.count_products == 4


def test_products_property(category_1):
    """Тестирование геттера вывода списка продуктов"""
    assert category_1.products == (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_add_product(category_1, product_1):
    """Тестирование добавления нового продукта в список продуктов"""
    assert len(category_1.products_in_list) == 3

    category_1.add_product(product_1)
    assert category_1.products == (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Samsung Galaxy S23 Ultra, 23100 руб. Остаток: 5 шт.\n"
    )

    assert len(category_1.products_in_list) == 4


def test_category_str(category_1):
    """Тестирование магического метода str класса Category"""
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."
    assert category_1.all_count_product == 27


def test_product_iterator(product_iterator):
    """Тестирование работы итератора"""
    iter(product_iterator)

    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23"
    assert next(product_iterator).name == "Iphone 15"
    assert product_iterator.index == 2
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_add_product_error(category_1):
    """Тестирование возникновения ошибки при попытке добавить в категорию не продукт"""
    with pytest.raises(TypeError):
        category_1.add_product("No")


def test_category_add_product_smartphone(category_1, smartphone1):
    """Тестирования успешного добавления в категорию объекта класса Smartphone"""
    category_1.add_product(smartphone1)
    assert category_1.products == (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_add_product_grass(category_1, grass1):
    """Тестирования успешного добавления в категорию объекта класса LawnGrass"""
    category_1.add_product(grass1)
    assert category_1.products == (
        "Samsung Galaxy S23, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Газонная трава, 500.0 руб. Остаток: 20 шт.\n"
    )


def test_middle_price(category_2):
    """Тестирование вычисления среднего ценника всех товаров"""
    assert category_2.middle_price() == 123000.0


def test__middle_price_zero_product():
    """Тестирование вычисления среднего ценника всех товаров при пустом списке товаров"""
    cat = Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром",
        products=[],)
    assert cat.middle_price() == 0
