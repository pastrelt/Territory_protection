from ICommand import *


class Landing(ICommand):
    """
    Посадка.
    """
    def __init__(self, drone: DronController):
        self.__drone = drone

    def execute(self):
        self.__drone.landing()