import requests# импортируем библиотеку для HTTP-запросов

BASE_URL = 'http://localhost:5000'


class ServerInterface:
    """
    Класс отправки сообщений с разлчных устройств: камеры, дрона ... на сервер.
    """
    def sending_messages(self, data):
        """
        Отправка сообщений в архив сервера MesagePool.
        """
        response = requests.post(f'{BASE_URL}/data ', json=data)
        if response.status_code == 200:
            logging.info(f'Информация отправлена на сервер: {response.json()}')
        else:
            logging.info(f'Ошибка при отправке уведомления на сервер: {response.status_code}')
