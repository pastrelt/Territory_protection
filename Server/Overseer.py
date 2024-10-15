from abc import ABC, abstractmethod
from Server.MesagePool import *


class Overseer(ABC):
    """
    Абстрактный класс, связывает информацию MesagePool со своими подклассами согласно их
    функциональной ответственности.
    """
    def __init__(self, mesage_pool: MesagePool):
        self.__mesage_pool = mesage_pool
        self.pool_cameras: int = 3

    def obtaining_information(self, server_request):# получение информации
        """
        Метод делает запрос в хранилище MesagePool и возвращает данные согласно запросов.
        :param server_request:
        :return: self.__mesage_pool.get_information(server_request)
        """
        return self.__mesage_pool.get_information(server_request)

    @abstractmethod
    def request(self):
        """
        Метод для однообразного формирования запросов классов Надзирателей
        :return:
        """
        server_request = {}
