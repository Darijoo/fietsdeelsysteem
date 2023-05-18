from fiets import Fiets

class Station:
    def __init__(self, name: str, id: str, cap: int, state: str):
        self.name = name            # stationsnaam
        self.id = id                # objectcode
        self.capacity = cap         # aantal plaatsen
        self.slots = []             # slots classes
        self.maintenance = False    # onderhoud

    def addBike(self, fiets: Fiets): # fiets toevoegen aan station
        if (len(self.slots) < self.capacity):
            self.slots.append(fiets)
            return True
        return False
    
    def removeBike(self, fiets: Fiets): # fiets verwijderen uit station
        if (fiets in self.slots): 
            self.slots.remove(fiets)
            return True
        return False
    
    def printSystemInfo(self, stations, username): # systeem informatie
        print(f"There are {len(stations)} stations in Antwerp.") 
        print(f"{len(username)} users are registered.")
    
    def printStationInfo(self): # station informatie
        print(f"Station {self.name} has {len(self.slots)} bikes.")
        print(f"It has a capacity of {self.capacity} bikes.")
        print(f"The station is currently {'not ' if not self.maintenance else ''}under maintenance.")
    
    def toonVrijeStations(self, stations): # toon alle stations met vrije plaatsen
        print("De volgende stations zijn beschikbaar:")
        for station in stations:
            if (station.capacity > len(station.slots)):
                print(f"Station {station.name} heeft nog {station.capacity - len(station.slots)} plaatsen vrij.")