from abc import ABC, abstractmethod


class AbstractCamera(abc):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def sending_video_stream(self):
        pass