from src.product import Product


class Category:
    """Класс для представления Категории продукта"""

    name: str
    description: str
    products: list

    count_categories = 0
    count_products = 0

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса Категории продукта. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.count_categories += 1
        Category.count_products += len(products) if products else 0

    @property
    def products(self):
        """Геттер для вывода списка продуктов в виде строки"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return products_str

    @property
    def products_in_list(self):
        """Геттер для корректного подсчета количества продуктов в категории"""
        return self.__products

    def add_product(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.count_products += 1
