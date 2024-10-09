
class MesagePool():
    @app.route("/data", methods=["POST"])
    def data(self):
        """
        Метод принмает данные от устройств.
        """
        data = request.get_json()
        self.save_inforation(data)
        return jsonify({'message': 'Уведомление получено'}), 200

    def save_inforation(self, data):
        """
        Метод записывает инфлормацию.
        """
        print("Информация записана")

    def set_information(self, dron_status):
        """
        Метод выдает инфлормацию.
        """
        data = {}
        return data