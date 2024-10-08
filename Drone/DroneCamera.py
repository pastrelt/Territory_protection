from Camerаs.AbstractCamera import *
from Drone import *


class DroneCamera(AbstractCamera):
    """
        Класс описания работы камеры дрона.
    """
    def camera_information(self):
        camera_index = 1
        camera_stop_flag = False
        camera_coordinates = {"latitude": -250.0, "longitude": 150.0}
        start_camera = SimpleStationaryCamera.get_information(None, camera_index, camera_coordinates, camera_stop_flag)


SimpleStationaryCamera.camera_information()