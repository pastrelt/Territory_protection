from Sersver.Overseer import *


class DroneAdding(Overseer):# добавление дрона
    def __init__(self, dron_status: Drone.Drone):
        self.dron_status = dron_status

    def obtaining_information(self):  # получение информации
        smp = Sersver.MesagePool.save_inforation(self.dron_status)


    def information_processing(self):  # обработка информации
        pass

    def solution(self): # решение
        pass