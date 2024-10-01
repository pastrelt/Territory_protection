from abc import ABC, abstractmethod


class ICommand(ABC):# интерфейс
    """
    Реализация патерна Сомманда,
    разделяем наши команды от логики управления нашими миссиями.
    """
    @abstractmethod
    def execute(self):
        pass