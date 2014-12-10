from parser.TracklistProvisioner import TracklistProvisioner
from bs4 import BeautifulSoup
from parser.TrackHistoryEntry import TrackHistoryEntry
from dateutil import parser
import re

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

        for node in news2Node.findAll(recursive=False, name='div'):
            retrievedTrack = TrackHistoryEntry()

            """ Parsing the thread title """
            trackNameNode = node.previousSibling
            if trackNameNode.name != 'table':
                continue

            trackNameNode = trackNameNode.find('tbody').find('tr').find('th').find('a')
            if trackNameNode is not None:
                retrievedTrack.Name = trackNameNode.text

            """ Parsing the play time and dj name """
            divs = node.findAll(recursive=False, name='div')
            if len(divs) >= 2:
                timePlayedNode = divs[1].find('table').find('tbody').find('tr').find('td')
                if timePlayedNode is None:
                    continue

                retrievedTrack.DJ = timePlayedNode.find('a').text

                match = re.search('([0-9:]+)', timePlayedNode.text)
                if len(match.groups()) != 0:
                    retrievedTrack.Date = parser.parse(match.group(1))

            retrievedTracks.append(retrievedTrack)

        return retrievedTracks