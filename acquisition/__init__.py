from acquisition.WeAreOneTracklistProvisioner import WeAreOneTracklistProvisioner
from acquisition.RequestsHttpConnection import RequestsHttpConnection
from core import WeAreOneRadio
import sys


def main():
    availableRadioStations = [
        WeAreOneRadio.CoretimeFM(),
        WeAreOneRadio.HardbaseFM(),
        WeAreOneRadio.TechnobaseFM(),
        WeAreOneRadio.HousetimeFM()
    ]

    radioStationIndex = -1 if "--radio" not in sys.argv else sys.argv.index("--radio")
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
        print("usage: tracklist --radio ({availableRadioStations})"
              .format(availableRadioStations='|'
                      .join([radioStation.Name.lower() for radioStation in availableRadioStations])))
        return

    tracklistProvisioner = WeAreOneTracklistProvisioner()
    [print(trackHistoryEntry) for trackHistoryEntry
     in tracklistProvisioner.Provide(targetRadioStation, RequestsHttpConnection())]

if __name__ == '__main__':
    main()