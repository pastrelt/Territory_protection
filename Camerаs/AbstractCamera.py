from abc import ABC, abstractmethod
from Camerаs.DefaultCameraProcessing import *
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

    def start(self):
        """
        Метод запускает процесс захвата видео с камеры и обработки каждого кадра.
        """
        logging.info(f'Камера {self.camera_index} запущена.')

        cap = cv2.VideoCapture(self.camera_index)
        while not self.camera_stop_flag:
            ret, frame = cap.read()
            if not ret:
                break

            ex_edges = DefaultCameraProcessing
            edges = ex_edges.process_frame(None,frame)
            penetration = ex_edges.detect_obstacle(None, edges, self.camera_index)
            if penetration:
                self.preparation_information()

            #edges = self.process_frame(frame)
            #self.detect_obstacle(edges)

            cv2.imshow(f'Камера {self.camera_index}', edges)

            if (cv2.getWindowProperty(f'Камера {self.camera_index}', cv2.WND_PROP_VISIBLE) < 1 or
                    cv2.waitKey(1) & 0xFF == ord('q')):#  этот код используется для завершения работы программы или
                                                # цикла, если окно камеры закрыто или пользователь нажал клавишу 'q'.
                self.camera_stop_flag = True
                break

            time.sleep(0.05)

        cap.release()
        cv2.destroyAllWindows()


    def preparation_information(self):
        """
        Подготовка информации
        """
        data = {
            'camera_index': self.camera_index,
            'coordinates': self.camera_coordinates
        }
        info = ServerInterface(data)
        info.receiving_information()

