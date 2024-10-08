from Sersver import ServerInterface

class ServerInterface:
    """
    Класс взаимодействия сервера с разлчными устройствами: камерой, дроном ...
    """
    def data_sorting(self):# сортировка данных по источникам получения
        pass

    def transfer_data_storage(self):# отправка данных в архив MesagePool
         pass

    @app.route("/camera_interface", methods=["POST"])
    def camera_interface():
        """
        Метод обрабатывае запрос камеры и если он подтверждается неоднократно (>100) отправляет дрон
        для съемки объекта нарушения, передавая координаты камеры.
        """













        global camera_request_count
        data = request.get_json()
        # Проверка наличия необходимых данных
        if 'camera_index' not in data or 'coordinates' not in data:
            logging.error('Некорректные данные: %s', data)
            return jsonify({'error': 'Некорректные данные'}), 400

        camera_index = data['camera_index']
        coordinates = data['coordinates']

        # Увеличение счетчика запросов для соответствующей камеры
        camera_request_count[str(camera_index)] += 1

        objective_control = 100# реагируем если событие повторяется более 100 раз, исключая случайности
        if camera_request_count[str(camera_index)] > objective_control:
            # Инициализируем управление дроном
            drone = drone_control(coordinates)
            # Сброс счетчика после отправки команды дрону
            camera_request_count[str(camera_index)] = 0

        return jsonify({'message': 'Уведомление получено'}), 200