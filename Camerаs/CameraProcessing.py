from abc import ABC, abstractmethod


class CameraProcessing(ABC):
    @abstractmethod
    def process_frame(self, frame):
        """
        Обрабатывает кадр, например, применяет фильтры или преобразования.
        :param frame: Исходный кадр из видео.
        :return: Обработанный кадр.
        """
        pass

    @abstractmethod
    def detect_obstacle(self, edges):
        """
        Обнаруживает препятствия на основе обработанных данных.
        :param edges: Данные о краях (например, после применения Canny).
        :return: True, если препятствие обнаружено, иначе False.
        """
        pass
