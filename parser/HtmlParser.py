from abc import ABCMeta, abstractmethod


class HtmlParser(metaclass=ABCMeta):
    def __init__(self, htmlContent):
        self.RawContent = htmlContent

    @abstractmethod
    def GetElementsByClass(self, name):
        pass