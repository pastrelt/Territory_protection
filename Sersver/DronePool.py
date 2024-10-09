from Sersver.DroneInterface import *


class DronePool:
    def __init__(self, data):
        self.data = data

    def get_information(self):
        print(f"Информация получена: {self.data}")

    def set_information(self):
        pass

