from abc import ABCMeta, abstractmethod


class HttpConnection(metaclass=ABCMeta):
    @abstractmethod
    def Get(self):
        pass

    @abstractmethod
    def Post(self, url, data):
        pass