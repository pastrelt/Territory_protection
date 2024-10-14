from abc import ABC, abstractmethod
from Camerаs.CameraProcessing import *
from Chat.ServerInterface import *
import logging
import time
import cv2

logging.basicConfig(level=logging.INFO, filemode="w", format='%(name)s - %(levelname)s - %(message)s')


class AbstractCamera(ABC):
    """
    Класс описывает работу камеры
    """
    def __init__(self, camera_index, camera_coordinates, camera_stop_flag):
        self.camera_index = camera_index
        self.camera_coordinates = camera_coordinates
        self.camera_stop_flag = camera_stop_flag

    def start(self, camera_processing: CameraProcessing):
        """
        Метод запускает процесс захвата видео с камеры и обработки каждого кадра.
        """
        logging.info(f'Камера {self.camera_index} запущена.')

        cap = cv2.VideoCapture(self.camera_index)
        server_interface = ServerInterface()# создаем экземпляр класса единственный раз!
        while not self.camera_stop_flag:
            ret, frame = cap.read()
            if not ret:
                break

            edges = camera_processing.process_frame(frame)
            penetration = camera_processing.detect_obstacle(edges, self.camera_index)

            if penetration:
                self.preparation_information(server_interface)

            cv2.imshow(f'Камера {self.camera_index}', edges)

            # Этот код используется для завершения работы программы или цикла,
            # если окно камеры закрыто или пользователь нажал клавишу 'q'.
            if (cv2.getWindowProperty(f'Камера {self.camera_index}', cv2.WND_PROP_VISIBLE) < 1
                    or cv2.waitKey(1) & 0xFF == ord('q')):
                self.camera_stop_flag = True
                break

            time.sleep(0.05)

        cap.release()
        cv2.destroyAllWindows()

    def preparation_information(self, server_interface: ServerInterface):
        """
        Подготовка данных
        """
        data = {
            'camera_index': self.camera_index,
            'coordinates': self.camera_coordinates
        }
        server_interface.sending_messages(data)