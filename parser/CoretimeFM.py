from parser.WeAreOneRadio import WeAreOneRadio


class CoretimeFM(WeAreOneRadio):
    def __init__(self):
        super(CoretimeFM, self).__init__("Coretime.FM", "http://www.coretime.fm/")

    def GetTracks(self):
        return []