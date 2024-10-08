from abc import ABC, abstractmethod
from MesagePool import


class Overseer(ABC):
    @abstractmethod
    def obtaining_information(self):# получение информации
        pass

    @abstractmethod
    def information_processing(self):# обработка информации
        pass

    