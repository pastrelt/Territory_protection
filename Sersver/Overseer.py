from abc import ABC, abstractmethod
from Sersver.MesagePool import *


class Overseer(ABC):
    def __init__(self, mesage_pool: MesagePool):
        self.mesage_pool = mesage_pool

    @abstractmethod
    def obtaining_information(self):# получение информации
        pass

    @abstractmethod
    def information_processing(self):# обработка информации
        pass

    @abstractmethod
    def solution(self):# решение
        pass