from abc import ABC, abstractmethod


class IFlightStrategy(ABC):
    """
    Реализуем патерн Стратегия.
    Интерфейс стратегии полета, определяет метод execute.
    """
    @abstractmethod
    def execute(self, commands: list):
        """
        Метод для выполнения списка команд в рамках стратегии.
        :param commands: Список команд для выполнения.
        """
        pass