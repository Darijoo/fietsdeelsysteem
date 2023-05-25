class Fiets:
    def __init__(self, bikeId, station=None, slot=None, inUse=False):
        self.id = bikeId
        self.station = station
        self.inUse = inUse
        self.currentLocation = None

    def moveToStation(self, destinationStation):
        if self.currentStation:
            self.currentStation.removeBike(self)
        destinationStation.addBike(self)
        self.currentStation = destinationStation
        print(f"The bike {self.id} has been moved to station {destinationStation.stationId}.")

    def printBikeInfo(self, stations, usernames):
        print(f"Bike ID: {self.id}")
        for station in stations:
            for slot in station.slots:
                if slot.bike == self:
                    print(f"Station: {station.name}")
                    print(f"Slot: {slot.slotId}")
        for user in usernames:
            if user.hasBike:
                print(f"User: {user.username}")
                break
        else:
            print("User: No user")
