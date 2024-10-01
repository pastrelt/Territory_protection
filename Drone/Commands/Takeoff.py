from ICommand import *


class Takeoff(ICommand):
    """
    Взлет
    """
    def __init__(self, drone: DronController):
        self.__drone = drone

    def execute(self):
        self.__drone.takeoff()