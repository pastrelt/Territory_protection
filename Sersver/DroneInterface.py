BASE_URL = 'http://localhost:5001'

class DroneInterface:
    """
    Класс взаимодействия с дроном
    """
    def sending_messages(self, data):
        """
        Отправка сообщений дрону
        """
        response = requests.post(f'{BASE_URL}/sending_messages', json=data)
        if response.status_code == 200:
            logging.info(f'Информация отправлена: {response.json()}')
        else:
            logging.info(f'Ошибка при отправке уведомления: {response.status_code}')


    @app.route("/receiving_messages", methods=["POST"])
    def receiving_messages():
        """
        Получение сообщений от дрона
        """
