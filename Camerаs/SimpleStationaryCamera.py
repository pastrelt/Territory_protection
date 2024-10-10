from Camerаs.AbstractCamerа import *
from Camerаs.DefaultCamerаProcessing import *


class SimpleStationaryCamerа(AbstractCamerа):
    """
    Класс описания работы конкретной простой стационарной камеры.
    """
    pass


if __name__ == "__main__":
    camera_index = 0
    camera_coordinates = {"latitude": 45.0, "longitude": 30.0}# Корректные координаты
    camera_stop_flag = False

    # Создаем экземпляр камеры
    simple_camera = SimpleStationaryCamerа(camera_index, camera_coordinates, camera_stop_flag)

    # Вызываем метод для получения информации от камеры
    camera_processing = DefaultCamerаProcessing()
    simple_camera.start(camera_processing)# Вызов метода родительского класса