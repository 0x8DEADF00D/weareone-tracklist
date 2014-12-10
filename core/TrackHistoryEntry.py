import datetime


class TrackHistoryEntry(object):
    def __init__(self):
        self.Name = ""
        self.Date = datetime.datetime.now()
        self.DJ = ""

    def __repr__(self):
        return "{time}: {name} (DJ: {dj})".format(dj=self.DJ, name=self.Name, time=self.Date.strftime("%d.%m.%Y %H:%M"))