from Sersver.MesagePool import *
import requests  # Импортируем библиотеку для HTTP-запросов

BASE_URL = 'http://localhost:5000'


class ServerInterface:
    """
    Класс получения сервером информации с разлчных устройств: камеры, дрона ...
    """
    def __init__(self, data):
        self.data = data

    def sending_information(self):
        """
        Отправка сообщений в архив сервера MesagePool
        """
        response = requests.post(f'{BASE_URL}/sending_information ', json=self.data)
        if response.status_code == 200:
            logging.info(f'Информация отправлена на сервер: {response.json()}')
        else:
            logging.info(f'Ошибка при отправке уведомления на сервер: {response.status_code}')
