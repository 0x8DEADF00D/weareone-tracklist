from acquisition.WeAreOneTracklistProvisioner import WeAreOneTracklistProvisioner
from acquisition.RequestsHttpConnection import RequestsHttpConnection
from core import WeAreOneRadio
import sys


def main():
    availableRadioStations = [
        WeAreOneRadio.CoretimeFM(),
        WeAreOneRadio.HardbaseFM(),
        WeAreOneRadio.TechnobaseFM(),
        WeAreOneRadio.HousetimeFM(),
        WeAreOneRadio.TrancebaseFM(),
        WeAreOneRadio.ClubtimeFM()
    ]

    if not len(sys.argv[1:]):
        print("usage: tracklist -radio ({availableRadioStations}) [-max max_track_count]"
              .format(availableRadioStations='|'
                      .join([radioStation.Name.lower() for radioStation in availableRadioStations])))
        return

    radioStationIndex = -1 if "-radio" not in sys.argv else sys.argv.index("-radio")
    targetRadioStation = WeAreOneRadio.TechnobaseFM()

    if radioStationIndex != -1 and len(sys.argv) > radioStationIndex + 1:
        targetRadioStation = [radioStation for radioStation
                              in availableRadioStations
                              if radioStation.Name.lower() == sys.argv[radioStationIndex + 1].lower()]
        if len(targetRadioStation) == 0:
            print("This radio station is not available, sorry")
            return
        else:
            targetRadioStation = targetRadioStation[0]
            print("Radio station: {name} ({url})".format(name=targetRadioStation.Name, url=targetRadioStation.BaseURL))
    else:
        print("No radio station was provided, please use the -radio switch")
        return

    maxTrackCountIndex = -1 if "-max" not in sys.argv else sys.argv.index("-max")
    maxTrackCount = 0
    if maxTrackCountIndex != -1 and len(sys.argv) > maxTrackCountIndex + 1:
        maxTrackCount = int(sys.argv[maxTrackCountIndex + 1])

    tracklistProvisioner = WeAreOneTracklistProvisioner()
    tracklist = tracklistProvisioner.Provide(targetRadioStation, RequestsHttpConnection())
    if not maxTrackCount:
        [print(trackHistoryEntry) for trackHistoryEntry
         in tracklist]
    else:
        print("Showing the first {trackCount} tracks".format(trackCount=maxTrackCount))
        [print(trackHistoryEntry) for trackHistoryEntry
         in tracklist[:maxTrackCount]]

if __name__ == '__main__':
    main()