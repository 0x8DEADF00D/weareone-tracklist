from parser.WeAreOneRadio import WeAreOneRadio


class HardbaseFM(WeAreOneRadio):
    def __init__(self):
        super(HardbaseFM, self).__init__("Hardbase.FM", "http://www.hardbase.fm/")

    def GetTracks(self):
        return []