from Camerаs.AbstractCamera import *
import logging

logging.basicConfig(level=logging.INFO, filemode="w", format='%(name)s - %(levelname)s - %(message)s')


class SimpleStationaryCamera(AbstractCamera):
    """
    Класс описания работы конкретной простой стационарной камеры.
    """
    def camera_information(self):
        logging.info(f'Получены данные с камеры №{self.camera_index}.')
        self.start()  # Вызов метода родительского класса


if __name__ == "__main__":
    camera_index = 0
    camera_coordinates = {"latitude": 45.0, "longitude": 30.0}  # Корректные координаты
    camera_stop_flag = False

    # Создаем экземпляр камеры
    simple_camera = SimpleStationaryCamera(camera_index, camera_coordinates, camera_stop_flag)

    # Вызываем метод для получения информации от камеры
    simple_camera.camera_information()