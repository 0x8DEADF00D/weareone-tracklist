from abc import ABCMeta, abstractmethod


class WeAreOneRadio(metaclass=ABCMeta):
    def __init__(self, name, baseurl):
        self.Name = name
        self.BaseURL = baseurl

    @abstractmethod
    def GetTracks(self):
        pass


