class ServerInterface:
    """
    Класс взаимодействия с устройствами
    """
    @app.route("/alert", methods=["POST"])
    def alert():
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
        # logging.info(f'Получено уведомление от камеры {camera_index} с координатами {coordinates}. '
        #              f'Текущий счетчик: {camera_request_count[str(camera_index)]}')

        # Проверка, превышает ли счетчик 100
        if camera_request_count[str(camera_index)] > 100:
            # Инициализируем управление дроном
            drone = drone_control(coordinates)
            # Сброс счетчика после отправки команды дрону
            camera_request_count[str(camera_index)] = 0

        return jsonify({'message': 'Уведомление получено'}), 200