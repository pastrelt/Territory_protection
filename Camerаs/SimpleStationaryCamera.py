from AbstractCamera import *
from CameraProcessing import *
import cv2# opencv-python
import logging

logging.basicConfig(level=logging.INFO, filemode="w", format='%(name)s - %(levelname)s - %(message)s')


class SimpleStationaryCamera(CameraProcessing, AbstractCamera):
    """
    Класс описания работы конкретной простой стационарной камеры.
    """
    def camera_information(self):
        logging.info(f'Получены данные с камеры №{self.camera_index}.')
        self.start()  # Вызов метода родительского класса

    def process_frame(self, frame):
        """
        Метод обрабатывает один кадр, чтобы подготовить его для дальнейшего анализа.
        Уменьшаем разрешение изображения в 2 раза и переводим в черно белое изображение.
        """
        frame_resized = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return edges

    def detect_obstacle(self, edges):
        """
        Метод анализирует обработанный кадр для обнаружения объектов.
        """
        number_borders = 100000 # количество границ
        if edges.sum() > number_borders:
            logging.info(f'Камера {self.camera_index}: Объект обнаружен')
            #self.send_alert_to_server()
        else:
            logging.info(f'Камера {self.camera_index}: Объект не обнаружен')


if __name__ == "__main__":
    camera_index = 0
    camera_coordinates = {"latitude": 45.0, "longitude": 30.0}  # Корректные координаты
    camera_stop_flag = False

    # Создаем экземпляр камеры
    simple_camera = SimpleStationaryCamera(camera_index, camera_coordinates, camera_stop_flag)

    # Вызываем метод для получения информации от камеры
    simple_camera.camera_information()