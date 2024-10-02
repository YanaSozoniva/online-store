from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin_repr(capsys):
    """Тестирование вывода информации об объекте в консоль при его создании"""
    Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=23100, quantity=5)
    massage = capsys.readouterr()
    assert massage.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 23100, 5)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
