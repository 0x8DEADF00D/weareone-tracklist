from parser.WeAreOneTracklistProvisioner import WeAreOneTracklistProvisioner
from parser.WeAreOneRadio import WeAreOneRadio
from parser.RequestsHttpConnection import RequestsHttpConnection


def main():
    tracklistProvisioner = WeAreOneTracklistProvisioner()
    print(tracklistProvisioner.Provide(WeAreOneRadio.TechnobaseFM(), RequestsHttpConnection()))
    pass


if __name__ == '__main__':
    main()