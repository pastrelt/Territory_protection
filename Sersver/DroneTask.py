from Sersver.Overseer import *
from Sersver.DronePool import *
from Sersver.DroneInterface import *


class DroneTask(Overseer):
    """
    Класс определяет есть ли информации для дрона и,
     при ее наличии, передает для отправки дрону на DroneInterface
    """
    def __init__(self, parameter: DronePool):
        self._parameter = parameter

    def information_processing(self, drone_interface: DroneInterface):
        information_camera = self._parameter('camera')
        data = self.obtaining_information(information_camera)
        if data != False:
            self.drone_interface.sending_messages(data)


if __name__ == "__main__":
    DroneTask.information_processing()