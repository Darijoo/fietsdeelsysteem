from fiets import Fiets

class Slot: # slots in stations
    def __init__(self, slot_id, bike=-1):
        self.id = slot_id
        self.in_gebruik = False
        self.bike = bike

    def setBike(self, bike: int):
        self.bike = bike

def getBike(self):
    return self.bike

def removeBikeFromSlot(self):
    self.bike = None

def printSlotInfo(self, stations, usernames):
    print(f"Slot ID: {self.id}")
    for station in stations:
        for slot in station.slots:
            if slot.id == self.id:
                print(f"Station: {station.name}")
                break
        else:
            continue
        break
    else:
        print("Station: No station")
    
    if self.bike is not None:
        print(f"Bike: {self.bike}")
    else:
        print("Bike: No bike")
    
    for user in usernames:
        if user.hasBike:
            print(f"User: {user.username}")
            break
    else:
        print("User: No user")

