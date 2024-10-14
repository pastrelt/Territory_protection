from Sersver.DroneInterface import *


class DronePool:
    def __init__(self, parameter):
        self.parameter = parameter

    def send(self):
        print(f"Информация отправлена: {self.parameter}")

    def set_information(self):
        pass

