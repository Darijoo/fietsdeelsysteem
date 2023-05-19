class Slot: # slots in stations
    def __init__(self, slot_id, bike=None):
        self.slot_id = slot_id
        self.bike = bike

    def assign_bike(self, bike):
        self.bike = bike

    def remove_bike(self):
        self.bike = None

    def printSlotInfo(self, stations, username):
        print(f"Slot ID: {self.slot_id}")
        for station in stations:
            for slot in station.slots:
                if slot.slot_id == self.slot_id:
                    print(f"Station: {station.name}")
                    break
        else:
            print("Station: Geen station")
        if self.bike != None:
            print(f"Fiets: {self.bike.fiets_id}")
        else:
            print("Fiets: Geen fiets")
        for user in username:
            if user.hasBike == True:
                print(f"Gebruiker: {user.username}")
                break
        else:
            print("Gebruiker: Geen gebruiker")