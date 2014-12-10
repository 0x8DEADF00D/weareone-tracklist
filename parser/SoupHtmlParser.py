from parser.HtmlParser import HtmlParser
from bs4 import BeautifulSoup


class SoupHtmlParser(HtmlParser):
    def __init__(self, htmlContent):
        super(SoupHtmlParser, self).__init__(htmlContent)
        self.Soup = BeautifulSoup(htmlContent)

    def GetElementsByClass(self, name):
        return self.Soup.find_all(attrs={'class': name})