from src.base_product import BaseProduct
from src.mixin_repr import MixinRepr


class Product(BaseProduct, MixinRepr):
    """Класс для представления Продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса продукты. Задает значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        else:
            self.quantity = quantity
        super().__init__()

    def __str__(self):
        """Метод, который отображает информацию об объекте класса Product для пользователей"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод возвращает сумму произведений цены на количество у двух объектов."""
        result = self.__price * self.quantity + other.__price * other.quantity
        return result

    @property
    def price(self):
        """Геттер для приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для приватного атрибута цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input("Вы уверены, что хотите снизить цену? y/n\n")
            if answer.lower() == "y":
                self.__price = new_price
            else:
                print("Цена осталась прежней")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, dict_product: dict, list_products: list = None):
        """Метод, который принимает на вход параметры товара в словаре и возвращает
        созданный объект класса Product"""
        if list_products:
            for product in list_products:
                if product.name == dict_product["name"]:
                    dict_product["quantity"] = dict_product["quantity"] + product.quantity

                    if product.price > dict_product["price"]:
                        dict_product["price"] = product.price

        name = dict_product["name"]
        description = dict_product["description"]
        price = dict_product["price"]
        quantity = dict_product["quantity"]
        return cls(name, description, price, quantity)
