from abc import ABC, abstractmethod
from Server.MesagePool import *


class Overseer(ABC):
    def __init__(self, mesage_pool: MesagePool):
        self.__mesage_pool = mesage_pool

    def obtaining_information(self, server_request):# получение информации
        return self.__mesage_pool.get_information(server_reques)

    @abstractmethod
    def choose_drone(self):# обработка информации
        pass