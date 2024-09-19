class Product:
    """Класс для представления Продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса продукты. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product: dict, list_products: list = None):
        """Метод, который принимает на вход параметры товара в словаре и возвращает
         созданный объект класса Product"""
        if list_products:
            for product in list_products:
                if product.name == dict_product['name']:
                    dict_product['quantity'] = dict_product['quantity'] + product.quantity

                    if product.price > dict_product['price']:
                        dict_product['price'] = product.price

        name = dict_product['name']
        description = dict_product['description']
        price = dict_product['price']
        quantity = dict_product['quantity']
        return cls(name, description, price, quantity)
