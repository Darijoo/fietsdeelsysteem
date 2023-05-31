from fiets import Fiets

class Slot: # slots in stations
    def __init__(self, id, inUse, bike):
        self.id = id
        self.inUse = False
        self.bike = bike

    def setBike(self, bike):
        self.bike = bike
        self.inUse = True
    
    def removeBike(self):
        self.bike = None
        self.inUse = False

