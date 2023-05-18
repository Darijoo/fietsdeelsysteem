
class Fiets:
    def __init__(self, fiets_id, inUse=False):
        self.inUse = False
        self.fiets_id = fiets_id

    def setInUse(self, inUse):
        self.inUse = inUse
        inUse = True
        return inUse
    

