import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from src.order import Order


@pytest.fixture()
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=23100, quantity=5
    )


@pytest.fixture()
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000, quantity=5)


@pytest.fixture()
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных"
        " функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture()
def category_2():
    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром," "станет вашим другом и помощником"
        ),
        products=[Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )


@pytest.fixture
def json_data():
    """Фикстура, создающая тестовый json"""

    test_dict = [
        {
            "name": "Смартфоны",
            "description": (
                "Смартфоны, как средство не только коммуникации,"
                " но и получение дополнительных функций для удобства жизни"
            ),
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]
    return test_dict


@pytest.fixture
def product_iterator(category_1):
    return ProductIterator(category_1)


@pytest.fixture
def smartphone1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def order1(product_2):
    return Order(product_2, 2)


@pytest.fixture
def order2(smartphone1):
    return Order(smartphone1, 16)
