Tracklist parser for WeAreOne radios
==================
This utility is capable of parsing the tracklist of the following WeAreOne radios:
* technobase.fm
* housetime.fm
* hardbase.fm
* coretime.fm
* clubtime.fm
* trancebase.fm

while printing the played tracks in the following format to stdout:

    tracklist -radio technobase.fm -max 3
    Radio station: Technobase.FM (http://www.technobase.fm/)
    Showing the first 3 tracks
    11.12.2014 22:57: Deepforces - Tribute To Dance (DJ: Patrick Ravage)
    11.12.2014 22:52: Rob Mayth - Herz An Herz (DJ: Patrick Ravage)
    11.12.2014 22:42: Fragrance - Don't Break My Heart (DJ: Patrick Ravage)

### Usage

`usage: tracklist -radio (coretime.fm|hardbase.fm|technobase.fm|housetime.fm) [-max max_track_count]`

* -radio is the radio station from where the tracklist will be parsed (use one of the mentioned radios above)
* -max is the maximum amount of entries being shown

### Requirements
* beautifulsoup4
* python-dateutil
* requests
* Python 3.4 (may also work with other versions of python, didn't test it)
