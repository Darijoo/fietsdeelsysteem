class Fiets:
    def __init__(self, id, station=None, slot=None, inUse=False):
        self.id = id
        self.station = station
        self.inUse = inUse
        self.currentLocation = None

    