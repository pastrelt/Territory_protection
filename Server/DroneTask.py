from Server.Overseer import *
from Server.DronePool import *
from Server.DroneInterface import *


class DroneTask(Overseer):
    """
    Класс определяет есть ли информации для дрона и,
     при ее наличии, выбирает дрона для отправки дрону информации на DroneInterface
    """
    def information_camera(self):
        data = self.obtaining_information(information_camera)
        if data != False:
            self.drone_interface.sending_messages(data)

    def choose_drone(self, choose_drone: DronePool, drone_interface: DroneInterface):
        drone = choose_drone()
        pass





if __name__ == "__main__":
#    DroneTask.information_camera()
    pass