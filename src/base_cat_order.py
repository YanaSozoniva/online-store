from abc import ABC, abstractmethod


class BaseCatOrder(ABC):
    """Абстрактный класс для классов Категория и Заказ"""

    @abstractmethod
    def __str__(self):
        pass
