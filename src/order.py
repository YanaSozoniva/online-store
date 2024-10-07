from src.product import Product
from src.base_cat_order import BaseCatOrder


class Order(BaseCatOrder):
    """Класс «Заказ», в котором содержится информация о том, какой товар был куплен, количество купленного товара,
    а также итоговая стоимость. В заказе может быть указан только один товар"""
    product: Product
    quantity: int
    total_cost: float

    def __init__(self, product: Product, quantity_buy: int):
        """Метод для инициализации экземпляра класса Заказ продукта. Задает значения атрибутам экземпляра."""
        self.product = product
        self.quantity = quantity_buy if quantity_buy <= product.quantity else product.quantity
        self.total_cost = product.price * self.quantity

    def __str__(self):
        """Метод, который отображает информацию об объекте класса Заказ для пользователей"""
        return (f"Заказ товара {self.product.name}, количество заказанного товара: {self.quantity} шт. "
                f"Сумма заказа {self.total_cost}")
