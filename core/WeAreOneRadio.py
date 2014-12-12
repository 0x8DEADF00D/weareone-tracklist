class WeAreOneRadio(object):
    def __init__(self, name, baseurl):
        self.Name = name
        self.BaseURL = baseurl

    def __repr__(self):
        return self.Name

    @staticmethod
    def TechnobaseFM():
        return WeAreOneRadio("Technobase.FM", "http://www.technobase.fm/")

    @staticmethod
    def HousetimeFM():
        return WeAreOneRadio("Housetime.FM", "http://www.housetime.fm/")

    @staticmethod
    def HardbaseFM():
        return WeAreOneRadio("Hardbase.FM", "http://www.hardbase.fm/")

    @staticmethod
    def CoretimeFM():
        return WeAreOneRadio("Coretime.FM", "http://www.coretime.fm/")

    @staticmethod
    def TrancebaseFM():
        return WeAreOneRadio("Trancebase.FM", "http://www.trancebase.fm/")

    @staticmethod
    def ClubtimeFM():
        return WeAreOneRadio("Clubtime.FM", "http://www.clubtime.fm/")