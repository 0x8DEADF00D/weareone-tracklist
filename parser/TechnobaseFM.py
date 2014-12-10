from parser.WeAreOneRadio import WeAreOneRadio


class TechnobaseFM(WeAreOneRadio):
    def __init__(self):
        super(TechnobaseFM, self).__init__("Technobase.FM", "http://www.technobase.fm/")

    def GetTracks(self):
        return []