from src.base_cat_order import BaseCatOrder
from src.exception import ZeroQuantityProduct
from src.product import Product


class Order(BaseCatOrder):
    """Класс «Заказ», в котором содержится информация о том, какой товар был куплен, количество купленного товара,
    а также итоговая стоимость. В заказе может быть указан только один товар"""

    product: Product
    quantity: int
    total_cost: float

    def __init__(self, product: Product, quantity_buy: int):
        """Метод для инициализации экземпляра класса Заказ продукта. Задает значения атрибутам экземпляра."""
        self.product = product
        try:
            if quantity_buy == 0:
                raise ZeroQuantityProduct("Нельзя заказать товар с нулевым количеством")
        except ZeroDivisionError as e:
            print(str(e))
        else:
            self.quantity = quantity_buy if quantity_buy <= product.quantity else product.quantity
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")
        self.total_cost = product.price * self.quantity

    def __str__(self):
        """Метод, который отображает информацию об объекте класса Заказ для пользователей"""
        return (
            f"Заказ товара {self.product.name}, количество заказанного товара: {self.quantity} шт. "
            f"Сумма заказа {self.total_cost}"
        )
