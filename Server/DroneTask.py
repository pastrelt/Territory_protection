from Server.Overseer import *
from Server.DronePool import *
from Server.DroneInterface import *


class DroneTask(Overseer):
    """
    Класс определяет есть ли информации для дрона.
    При ее наличии выбирает дрона и отправляет ему сообщение.
    """
    def request(self, choose_drone: DronePool, drone_interface: DroneInterface):
        """
        Запрос информамции, которвя определит начало работы дрона.
        """
        for camera_index in range(self.pool_cameras):
            camera_id = f"camera_{str(camera_index)}"
            server_request = {camera_id: camera_index}
            result = self.obtaining_information(server_request)
            if result != False:# есть сообщение от камеры
                choose_drone.select_drone(drone_interface)# получен дрон для запуска
                drone_interface.sending_messages(result)#зотправляем информацию дрону
                return







if __name__ == "__main__":
    drone_task = DroneTask()
    choose_drone = DronePool()
    drone_interface = DroneInterface()

    drone_task.request(choose_drone, drone_interface)
