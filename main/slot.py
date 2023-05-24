from fiets import Fiets

class Slot: # slots in stations
    def __init__(self, slot_id, fiets=-1):
        self.id = slot_id
        self.in_gebruik = False
        self.fiets = fiets

    def setFiets(self, fiets: int):
        self.fiets = fiets

    def getFiets(self):
        return self.fiets

    def verwijderFietsUitSlot(self):
        self.fiets = None

    def printSlotInfo(self, stations, username):
        print(f"Slot ID: {self.id}")
        for station in stations:
            for slot in station.slots:
                if slot.slot_id == self.id:
                    print(f"Station: {station.name}")
                    break
        else:
            print("Station: Geen station")
        if self.fiets != None:
            print(f"Fiets: {self.fiets}")
        else:
            print("Fiets: Geen fiets")
        for user in username:
            if user.heeftFiets == True:
                print(f"Gebruiker: {user.username}")
                break
        else:
            print("Gebruiker: Geen gebruiker")
