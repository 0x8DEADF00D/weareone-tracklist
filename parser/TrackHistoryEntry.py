class TrackHistoryEntry(object):
    def __init__(self):
        self.Name = ""
        self.Time = ""
        self.DJ = ""

    def __repr__(self):
        return "{dj}: {name} ({time})".format(dj=self.DJ, name=self.Name, time=self.Time)