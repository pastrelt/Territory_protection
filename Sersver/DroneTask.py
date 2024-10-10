from Sersver.Overseer import *


class DroneTask(Overseer):# задача дрона
    def obtaining_information(self):# получение информации
        request_information_camera = "Есть информация от камеры?"
        signal = self.mesage_pool.set_information(request_information_camera)
        if signal!= False:
            solution(signal)
        else:



    def information_processing(self):# обработка информации
        pass

    def solution(self, signal):# решение
        pass

if __name__ == "__main__":
    DroneTask.obtaining_information()