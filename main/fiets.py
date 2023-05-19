
class Fiets:
    def __init__(self, fiets_id, station=None, slot=None, in_use=False):
        self.fiets_id = fiets_id
        self.station = station
        self.slot = slot
        self.in_use = in_use

    def printFietsInfo(self, stations, username):
        print(f"Fiets ID: {self.fiets_id}")
        for station in stations:
            for slot in station.slots:
                if slot.bike == self:
                    print(f"Station: {station.name}")
                    print(f"Slot: {slot.slot_id}")
        for user in username:
            if user.hasBike == True:
                print(f"Gebruiker: {user.username}")
                break
        else:
            print("Gebruiker: Geen gebruiker")
    

