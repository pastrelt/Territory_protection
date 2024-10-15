from Server.DroneInterface import *

class DronePool:
    '''
    Класс обеспечивает подготовку информации для передачи дрону
    '''
    def __init__(self):
        self.basic_drones_status = {'drone_1': True, 'drone_2': False, 'drone_3': True}

    def select_drone(self, drone_interface: DroneInterface):
        """
        Метод помогает выбрать дрона, согласно его текущего статуса
        :param drone_interface:
        :return: real_status_drone
        """
        for drone_name, basic_status in self.basic_drones_status.items():
            if basic_status:
                real_status_drone = drone_interface.drone_status(drone_name, basic_status)
                if real_status_drone:
                    return real_status_drone


if __name__ == "__main__":
    drone = DronePool()
    drone_interface = DroneInterface()
    result = drone.select_drone(drone_interface)
    print(result)  # Выводим результат









# from Server.DroneInterface import *
#
#
# class DronePool:
#     '''
#     Класс содержит информацию о всех доронах системы
#     '''
#     def __init__(self):
#         #self.drone_interface = drone_interface
#         self.drone_pool = {'drone_1': True, 'drone_2': True, 'drone_3': True}
#
#     def choose_drone(self, drone_interface: DroneInterface):
#         for drone in self.drone_pool.items():
#             print(drone)
#             #drone_interface = DroneInterface()
#             drone_interface.sending_messages(drone)
#             return drone
#
#
# if __name__ == "__main__":
#     drone = DronePool()
#     drone_interface = DroneInterface()
#     drone.choose_drone(drone_interface)