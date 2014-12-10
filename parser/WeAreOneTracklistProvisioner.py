from parser.TracklistProvisioner import TracklistProvisioner
from bs4 import BeautifulSoup

class WeAreOneTracklistProvisioner(TracklistProvisioner):
    def Provide(self, radio, httpConnection):
        responseContent = httpConnection.Get(radio.BaseURL + "tracklist")
        soup = BeautifulSoup(responseContent)

        retrievedTracks = []
        news2Node = soup.find(attrs={'class': 'news2'})
        if news2Node is None:
            return retrievedTracks

        news2Node = news2Node.find('div')
        if news2Node is None:
            return retrievedTracks

        for node in news2Node.findAll(recursive=False, name='table'):
            trackNameNode = node.find('tbody').find('tr').find('th').find('a')
            if trackNameNode is not None:
                retrievedTracks.append(trackNameNode.text)

        return retrievedTracks