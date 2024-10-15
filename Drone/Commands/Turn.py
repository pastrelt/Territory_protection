from ICommand import *


class Turn(ICommand):
    """
    Поворот.
    """
    def __init__(self, drone: DronController, degree: float):
        self.__drone = drone
        self.__degree = degree

    def execute(self):
        self.__drone.turn(self.__degree)