from ICommand import *


class MoveForward(ICommand):
    """
    Движение вперед.
    """
    def __init__(self, drone: DronController, coordinates):
        self.__drone = drone
        self.__coordinates = coordinates

    def execute(self):
        self.__drone.move_forward(self.__coordinates)