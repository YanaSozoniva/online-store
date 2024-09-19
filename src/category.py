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
        self.products = products if products else []

        Category.count_categories += 1
        Category.count_products += len(products) if products else 0
