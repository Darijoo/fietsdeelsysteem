from fiets import Fiets
from slot import Slot

class Station:
    def __init__(self, name: str, id: str, cap: int, state: str):
        self.name = name            # stationsnaam
        self.id = id                # objectcode
        self.capacity = cap         # aantal plaatsen
        self.slots = [Slot() for i in range(cap)] # plaatsen
        if state == "IN_GEBRUIK":
            self.maintenance = False
        else:
            self.maintenance = True


    def addBike(self, bike): #werkt
        for slot in self.slots:
            if not slot.inUse:
                slot.setBike(bike)
                bike.station = self.id
                print(f"Bike {bike.id} added to station {self.name}.")
                return True
        return False
    
    def returnBike(self, bike):
        self.addBike(bike)

    def withdrawBike(self):
        for slot in self.slots:
            if slot.inUse:
                bike = slot.removeBike()
                print("Bike withdrawn.")
                return bike
            
    def withdrawBikes(self):
        bikes = []
        while self.getBikeCountPercentage() > 50:
            for slot in self.slots:
                if self.getBikeCountPercentage() <= 40:
                    return bikes
                if slot.inUse:
                    bike = slot.removeBike()
                    bikes.append(bike)
        return bikes
    
    def hasMoreThanEnoughBikes(self):
        if self.getBikeCountPercentage() > 50:
            return True
        
    def hasLessThanEnoughBikes(self):
        if self.getBikeCountPercentage() < 35:
            return True

    def getAvailableBikes(self):
        return [bike for bike in self.bikes if not bike.inUse]

    

    def printStationInfo(self):
        print(f"Station {self.name} has {self.getBikeCount()} bike(s).")
        print(f"It has a capacity of {self.capacity} bike(s).")
        print(f"The station is currently {'not ' if not self.maintenance else ''}under maintenance.")

    def getFreeSlot(self):
        for slot in self.slots:
            if slot.inUse == False:
                return slot
        return None

    def hasFreeSlot(self): #werkt
        for slot in self.slots:
            if slot.inUse == False:
                return True
        return False

    def getBikeCount(self): #werkt
        count = 0
        for slot in self.slots:
            if slot.inUse:
                count += 1
        return count
    
    def getBikeCountPercentage(self): #werkt
        return self.getBikeCount() / self.capacity * 100
    
    def hasBike(self): #werkt
        for slot in self.slots:
            if slot.inUse:
                return True
        return False