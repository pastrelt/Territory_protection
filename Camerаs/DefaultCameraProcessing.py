from Camerаs.CameraProcessing import *
import cv2# opencv-python
import logging

logging.basicConfig(level=logging.INFO, filemode="w", format='%(name)s - %(levelname)s - %(message)s')


class DefaultCameraProcessing(CameraProcessing):
    def process_frame(self, frame):
        """
        Метод обрабатывает один кадр, чтобы подготовить его для дальнейшего анализа.
        Уменьшаем разрешение изображения в 2 раза и переводим в черно белое изображение.
        """
        frame_resized = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
        gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return edges

    def detect_obstacle(self, edges, camera_index):
        """
        Метод анализирует обработанный кадр для обнаружения объектов.
        """
        number_borders = 100000# количество границ
        if edges.sum() > number_borders:
            logging.info(f'Камера {camera_index}: Объект обнаружен')
            return True
        else:
            logging.info(f'Камера {camera_index}: Объект не обнаружен')
            return False





        # Заначка, на случай если решу подключить несколько стационарных камеры
        # Еще надо решить тему с разными потоками на камеры
        #
        #
        #
        # global camera_request_count
        #
        #
        # # Увеличение счетчика запросов для соответствующей камеры
        # camera_request_count[str(camera_index)] += 1
        #
        # objective_control = 100# реагируем если событие повторяется более 100 раз, исключая случайности
        # if camera_request_count[str(camera_index)] > objective_control:
        #     # Инициализируем управление дроном
        #     drone = drone_control(coordinates)
        #     # Сброс счетчика после отправки команды дрону
        #     camera_request_count[str(camera_index)] = 0
        #
        # return jsonify({'message': 'Уведомление получено'}), 200