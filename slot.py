from fiets import Fiets
import copy

class Slot: # slots in stations
    def __init__(self):
        self.inUse = False
        self.bike = None

    def setBike(self, bike):
        self.bike = bike
        self.inUse = True
    
    def removeBike(self):
        bike = copy.deepcopy(self.bike)
        self.bike = None
        self.inUse = False
        return bike

    def getBike(self):
        return self.bike