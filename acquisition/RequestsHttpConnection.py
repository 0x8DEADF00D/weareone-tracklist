from acquisition.HttpConnection import HttpConnection
from acquisition.ConnectionFailedException import ConnectionFailedException
import requests

class RequestsHttpConnection(HttpConnection):
    def Get(self, url):
        res = requests.get(url)
        if(res.status_code != 200):
            raise ConnectionFailedException("Connection to URL {url} failed while performing a HTTP GET request"
                                            .format(url=url))
        else:
            return res.text

    def Post(self, url, data):
        pass
