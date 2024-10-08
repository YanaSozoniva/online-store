class ProductIterator:
    """Вспомогательный класс, с помощью которого можно перебирать товары одной категории"""

    def __init__(self, category_obg):
        """Конструктор для инициализации экземпляра класса."""
        self.category = category_obg
        self.index = 0

    def __iter__(self):
        """Возвращает итератор."""
        self.index = 0
        return self

    def __next__(self):
        """Возвращает следующий продукт из списка товаров в категории."""
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
