
class Fiets:
    def __init__(self):
        self.inUse = False
        self.timeLeft = 60
        self.lastMaintenance = []

class Station:
    def __init__(self, name: str, id: str, cap: int, types: list, state: str):
        self.name = name            # stationsnaam
        self.id = id                # objectcode
        self.capacity = cap         # aantal plaatsen
        self.slots = []             # slots classes
        self.maintenance = False    # onderhoud
        self.types = types          # type fietsen
        
    def doesBikeFit(self, bikeType):
        for type in self.types:
            if (type == bikeType):
                return True
        return False

    def addBike(self, fiets: Fiets):
        if (len(self.slots) < self.capacity):
            self.slots.append(fiets)
            return True
        return False
    
    def printSystemInfo(self, stations, username):
        print(f"There are {len(stations)} stations in Antwerp.") 
        print(f"{len(username)} users are registered.")
    
    def printStationInfo(self):
        print(f"Station {self.name} has {len(self.slots)} bikes.")
        print(f"It has a capacity of {self.capacity} bikes.")
        print(f"The station is currently {'not ' if not self.maintenance else ''}under maintenance.")
        print(f"The station has the following bike types: {', '.join(self.types)}")
    
    def toonVrijeStations(self, stations):
        print("De volgende stations zijn beschikbaar:")
        for station in stations:
            if (station.capacity > len(station.slots)):
                print(f"Station {station.name} heeft nog {station.capacity - len(station.slots)} plaatsen vrij.")


class Gebruiker:
    def __init__(self, username):
        self.username = username # gebruikersnaam
        self.hasBike = False

    def geefAlleGebruikers(self, username):
        for user in username:
            print(user.username)

    def geefTotaalAantalGebruikers(self, username):
        print(f"Er zijn {len(username)} gebruikers geregistreerd.")

    def geefGebruikerInfo(self, username):
        print(f"De gebruiker {self.username} heeft een fiets: {'ja' if self.hasBike else 'nee'}")

    def voegGebruikerToe(self, username):
        username.append(self)
        print(f"De gebruiker {self.username} is toegevoegd.")

class Slot:
    def __init__(self, slot_id, bike=None):
        self.slot_id = slot_id
        self.bike = bike

    def assign_bike(self, bike):
        self.bike = bike

    def remove_bike(self):
        self.bike = None

class Transporter(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.transport_history = []

    def transport_bike(self, bike, source_station, destination_station):
        source_slot = source_station.slots[bike.slot_id]
        destination_slot = destination_station.slots[bike.slot_id]

        source_slot.remove_bike()
        destination_slot.assign_bike(bike)

        self.transport_history.append({
            "bike_id": bike.bike_id,
            "source_station_id": source_station.station_id,
            "destination_station_id": destination_station.station_id
        })


class Logger:
    def __init__(self):
        self.log = []

    def log_movement(self, bike_id, source_station_id, destination_station_id):
        self.log.append({
            "bike_id": bike_id,
            "source_station_id": source_station_id,
            "destination_station_id": destination_station_id
        })
