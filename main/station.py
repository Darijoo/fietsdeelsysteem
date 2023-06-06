from fiets import Fiets
from slot import Slot

class Station:
    def __init__(self, name: str, id: str, cap: int, state: str):
        self.name = name            # stationsnaam
        self.id = id                # objectcode
        self.capacity = cap         # aantal plaatsen
        self.slots = [Slot() for i in range(cap)] # plaatsen
        self.maintenance = state    # onderhoud


    def addBike(self, bike):
        for slot in self.slots:
            if not slot.inUse:
                slot.setBike(bike)
                bike.station = self.id
                return True
            return False

    def removeBike(self):
        for slot in self.slots:
            if slot.inUse:
                slot.removeBike()
                return True
            return False

    def getAvailableBikes(self):
        return [bike for bike in self.bikes if not bike.inUse]

    

    def printStationInfo(self, station):
        print(f"Station {station.name} has {station.getBikeCount()} bike(s).")
        print(f"It has a capacity of {station.capacity} bike(s).")
        print(f"The station is currently {'not ' if not station.maintenance else ''}under maintenance.")

    def getFreeSlot(self):
        for slot in self.slots:
            if slot.inUse == False:
                return slot
        return None

    def hasFreeSlot(self):
        for slot in self.slots:
            if slot.inUse == False:
                return True
        return False

    def getBikeCount(self):
        count = 0
        for slot in self.slots:
            if slot.inUse:
                count += 1
        return count