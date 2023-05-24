
class Fiets:
    def __init__(self, fiets_id, station=None, slot=None, in_gebruik=False):
        self.fiets_id = fiets_id
        self.station = station
        self.slot = slot
        self.in_gebruik = in_gebruik
        self.huidige_locatie = None

    def verplaatsNaarStation(self, bestemming_station):
        if self.huidig_station:
            self.huidig_station.verwijderFiets(self)
        bestemming_station.voegFietsToe(self)
        self.huidig_station = bestemming_station
        print(f"De fiets {self.fiets_id} is verplaatst naar station {bestemming_station.station_id}.")


    def printFietsInfo(self, stations, username):
        print(f"Fiets ID: {self.fiets_id}")
        for station in stations:
            for slot in station.slots:
                if slot.fiets == self:
                    print(f"Station: {station.name}")
                    print(f"Slot: {slot.slot_id}")
        for user in username:
            if user.heeftFiets == True:
                print(f"Gebruiker: {user.username}")
                break
        else:
            print("Gebruiker: Geen gebruiker")
    

