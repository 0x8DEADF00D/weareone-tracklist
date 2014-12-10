from parser.WeAreOneRadio import WeAreOneRadio


class HousetimeFM(WeAreOneRadio):
    def __init__(self):
        super(HousetimeFM, self).__init__("Housetime.FM", "http://www.housetime.fm/")

    def GetTracks(self):
        return []