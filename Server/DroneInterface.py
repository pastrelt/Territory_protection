import requests

BASE_URL = 'http://localhost:5001'

class DroneInterface:
    """
    Класс взаимодействия с дроном.
    """
    def drone_status(self, dron_id, data):
        try:
            response = requests.post(f'{BASE_URL}/{dron_id}', json=data)
            if response.status_code == 200:
                logging.info(f"Получен статус тостояния от дрона: {response.json()}")
                return  response.json()['real_status_drone']
            else:
                logging.info("Ошибка при отправке запроса:", response.status_code)
        except Exception as e:
            logging.info("Ошибка при подключении к серверу:", e)

    def sending_messages(self, data):
        """
        Отправка сообщений дрону
        """
        response = requests.post(f'{BASE_URL}/sending_messages', json=data)
        if response.status_code == 200:
            logging.info(f'Информация отправлена: {response.json()}')
        else:
            logging.info(f'Ошибка при отправке уведомления: {response.status_code}')