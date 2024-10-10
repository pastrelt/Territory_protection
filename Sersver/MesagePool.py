import requests
import logging

logging.basicConfig(level=logging.INFO, filemode="w", format='%(name)s - %(levelname)s - %(message)s')


class MesagePool():
    @app.route("/data", methods=["POST"])
    def data(self):
        """
        Метод принмает данные от ServerInterface.
        """
        data = request.get_json()
        self.save_inforation(data)
        return jsonify({'message': 'Уведомление получено'}), 200

    def save_inforation(self, data):
        """
        Метод записывает инфлормацию.
        """
        print("Информация записана")

    def set_information(self, server_request):
        """
        Метод выдает инфлормацию.
        """
        data = {}# предполагается вместо этого оператора вставить блок поиска информации
        if data != None:
            return data
        else:
            return False
