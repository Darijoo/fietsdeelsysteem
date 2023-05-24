from fiets import Fiets

class Station:
    def __init__(self, name: str, id: str, cap: int, state: str):
        self.name = name            # stationsnaam
        self.id = id                # objectcode
        self.capaciteit = cap         # aantal plaatsen
        self.slots = []             # slots classes
        self.onderhoud = False    # onderhoud
        self.fiets = []             # fietsen classes

    def voegFietsToe(self, fiets: Fiets): # fiets toevoegen aan station
        if (len(self.slots) < self.capaciteit):
            self.slots.append(fiets)
            return True
        return False
    
    def verwijderfiets(self, fiets: Fiets): # fiets verwijderen uit station
        if (fiets in self.slots): 
            self.slots.remove(fiets)
            return True
        return False
    
    def getBeschikbareFietsen(self):
        return [fiets for fiets in self.fiets if not fiets.in_gebruik]
    
    def printSystemInfo(self, stations, username): # systeem informatie
        print(f"There are {len(stations)} stations in Antwerp.") 
        print(f"{len(username)} users are registered.")
    
    def printStationInfo(self): # station informatie
        print(f"Station {self.name} has {len(self.slots)} fiets.")
        print(f"It has a capaciteit of {self.capaciteit} fiets.")
        print(f"The station is currently {'not ' if not self.onderhoud else ''}under onderhoud.")
    
    def toonVrijeStations(self, stations): # toon alle stations met vrije plaatsen
        print("De volgende stations zijn beschikbaar:")
        for station in stations:
            if (station.capaciteit > len(station.slots)):
                print(f"Station {station.name} heeft nog {station.capaciteit - len(station.slots)} plaatsen vrij.")