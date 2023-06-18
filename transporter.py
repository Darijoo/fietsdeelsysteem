
class Transporter(): # fietsen verplaatsen
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hasBike = False
        self.bikes = []

        self.transport_geschiedenis = []

    def takeBikes(self, station):
        if not self.hasBike:
            if station.hasBike():
                if station.getBikeCountPercentage() > 50:
                    self.hasBike = True
                    self.bikes = station.withdrawBikes()
                    for bike in self.bikes:
                        bike.inUse = True
                    print(f"The transporter {self.name} now has {len(self.bikes)} bikes.")
            else:
                print(f"The station {station.name} has no bikes.")
        else:
            print(f"The transporter {self.name} already has bikes.")

    def returnBikes(self, station):
        if self.hasBike:
            self.hasBike = False
            for bike in self.bikes:
                bike.inUse = False
                station.returnBike(bike)
            print(f"The transporter {self.name} no longer has bikes.")
        else:
            print(f"The transporter {self.name} has no bikes to return.")

    def startBikePickup(self, stations):
        for station in stations:
            if station.hasMoreThanEnoughBikes():
                    self.takeBikes(station)
                    break
            
    def startBikeDropoff(self, stations):
        for station in stations:
            if station.hasLessThanEnoughBikes():
                self.returnBikes(station)
                break
                        
