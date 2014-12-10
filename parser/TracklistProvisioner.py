from abc import ABCMeta, abstractmethod


class TracklistProvisioner(metaclass=ABCMeta):
    @abstractmethod
    def Provide(self, radio, httpConnection, htmlParser):
        pass