from fiets import Fiets

class Slot: # slots in stations
    def __init__(self):
        self.inUse = False
        self.bike = None

    def setBike(self, bike):
        self.bike = bike
        self.inUse = True
    
    def removeBike(self):
        self.bike = None
        self.inUse = False

    def getBike(self):
        return self.bike