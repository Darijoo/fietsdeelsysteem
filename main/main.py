# from jsonParser import stations, username
from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from pick import pick

bigbrain = Controller(numBikes=3620, numUsers=4200)
users = bigbrain.gen.getUsers()
gebruiker = Gebruiker(users, users)

stations = bigbrain.gen.getStations()

valid_responses = []
for i in range(13):
    valid_responses.append(i)

username = input("Geef gebruiksernaam ")
if username not in bigbrain.gen.getUsers():
    bigbrain.gen.addUser(username)
while True:
    print("Wat wil je doen?")
    print("1. fiets huren")
    print("2. fiets terugbrengen")
    print("3. Station informatie")
    print("4. Gebruiker informatie")
    print("5. Toon alle beschikbare stations")
    print("6. exporteer info als web pagina")
    print("7. Exit")
    response = input("Kies een optie: ")
    try:
        response = int(response)
    except Exception as e:
        print(e)

    if response not in valid_responses:
        print("Ongeldige optie, probeer opnieuw.")
        continue

    match(response):
        case 1:
            bike = None
            while not bike:
                for i, station in enumerate(stations):
                    print(f"{i + 1}. {station.name}")
                station_number = int(input("Geef het nummer van het station: "))
                if station_number < 1 or station_number > len(stations):
                    print("Ongeldig stationnummer. Probeer opnieuw.")
                    continue
                station = stations[station_number - 1]
                bike = bigbrain.getFreeBike(station)
                if not bike:
                    print("Geen fiets in dit station. Kies een ander station.")
                    continue

        case 2:
            bike = None
            while(not bike):
                stationName = pick([station.name for station in stations], "Kies een station: ", indicator="=>")
                station = bigbrain.getStationByName(stationName)
                if not station:
                    print("Kan station niet vinden. Check spelling")
                    continue
                bike = bigbrain.getFreeBike(station)
                if not bike:
                    print("Geen fiets in dit station, geef een ander station")
                    continue
        case 3:
            station = bigbrain.getStationByName(input("geef naam van station: "))
            if not station:
                print("Kan station niet vinden. Check spelling")
                continue
            station.printStationInfo()

        case 4:
            user = Gebruiker(input("Geef gebruikersnaam: "))
            if not user:
                print("Kan gebruiker niet vinden. Check spelling")
                continue
            bigbrain.printUserInfo(user)
        
