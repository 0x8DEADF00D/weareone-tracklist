from abc import ABCMeta, abstractmethod


class HttpConnection(metaclass=ABCMeta):
    @abstractmethod
    def Get(self, url):
        pass

    @abstractmethod
    def Post(self, url, data):
        pass