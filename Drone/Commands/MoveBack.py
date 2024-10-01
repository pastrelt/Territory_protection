from ICommand import *


class MoveBack(ICommand):
    """
    Движение назад
    """
    def __init__(self, drone: DronController, coordinates):
        self.__drone = drone
        self.__coordinates = coordinates

    def execute(self):
        self.__drone.move_back(self.__coordinates)