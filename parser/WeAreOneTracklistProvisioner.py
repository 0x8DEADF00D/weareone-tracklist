from parser.TracklistProvisioner import TracklistProvisioner


class WeAreOneTracklistProvisioner(TracklistProvisioner):
    def Provide(self, radio, httpConnection):
        return []