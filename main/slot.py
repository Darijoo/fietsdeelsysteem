class Slot: # slots in stations
    def __init__(self, slot_id, fiets=None):
        self.slot_id = slot_id
        self.fiets = fiets

    def assign_fiets(self, fiets):
        self.fiets = fiets

    def verwijderFietsUitSlot(self):
        self.fiets = None

    def printSlotInfo(self, stations, username):
        print(f"Slot ID: {self.slot_id}")
        for station in stations:
            for slot in station.slots:
                if slot.slot_id == self.slot_id:
                    print(f"Station: {station.name}")
                    break
        else:
            print("Station: Geen station")
        if self.fiets != None:
            print(f"Fiets: {self.fiets.fiets_id}")
        else:
            print("Fiets: Geen fiets")
        for user in username:
            if user.heeftFiets == True:
                print(f"Gebruiker: {user.username}")
                break
        else:
            print("Gebruiker: Geen gebruiker")