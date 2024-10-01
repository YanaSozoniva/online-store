from src.product import Product


class LawnGrass(Product):
    """Класс для представления Трава газонная, потомок класса Product"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Конструктор для инициализации экземпляра класса Трава газонная."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
