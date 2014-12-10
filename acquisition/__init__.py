from acquisition.WeAreOneTracklistProvisioner import WeAreOneTracklistProvisioner
from acquisition.RequestsHttpConnection import RequestsHttpConnection
from core import WeAreOneRadio


def main():
    tracklistProvisioner = WeAreOneTracklistProvisioner()
    print(tracklistProvisioner.Provide(WeAreOneRadio.TechnobaseFM(), RequestsHttpConnection()))
    pass


if __name__ == '__main__':
    main()