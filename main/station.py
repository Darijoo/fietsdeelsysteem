from fiets import Fiets

class Station:
    def __init__(self, name: str, id: str, cap: int, state: str):
        self.name = name            # stationsnaam
        self.id = id                # objectcode
        self.capacity = cap         # aantal plaatsen
        self.slots = []              # slots classes
        self.maintenance = False    # onderhoud
        self.bikes = []             # fietsen classes

    def addBike(self, bike):
        if len(self.slots) < self.capacity:
            self.bikes.append(bike)
            return True
        return False

    def removeBike(self, bike):
        if bike in self.slots:
            self.slots.remove(bike)
            return True
        return False

    def getAvailableBikes(self):
        return [bike for bike in self.bikes if not bike.inUse]

    def printSystemInfo(self, stations, usernames):
        print(f"There are {len(stations)} stations in Antwerp.")
        print(f"{len(usernames)} users are registered.")

    def printStationInfo(self, stations, usernames):
        print(f"Station {self.name} has {len(self.slots)} bike(s).")
        print(f"It has a capacity of {self.capacity} bike(s).")
        print(f"The station is currently {'not ' if not self.maintenance else ''}under maintenance.")

    def showFreeStations(self, stations):
        print("The following stations have available slots:")
        for station in stations:
            if station.capacity > len(station.slots):
                print(f"Station {station.name} has {station.capacity - len(station.slots)} free slot(s).")
 
    def getFreeSlot(self):
        for slot in self.slots:
            if not slot.in_use:
                return slot
        return None

