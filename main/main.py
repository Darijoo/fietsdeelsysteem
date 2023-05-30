# from jsonParser import stations, username
from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from pick import pick

bigbrain = Controller()

# station = Station("Example Station", "123", 10,"In gebruik")
# station.printSystemInfo(stations, username)
stations = bigbrain.gen.getStations()

valid_responses = []
for i in range(13):
    valid_responses.append(i)

username = input("Geef gebruiksernaam ")

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
            while(not bike):
                print([station.name for station in stations])
                station = bigbrain.getStationByName(input("Geef naam van station: "))
                if not station:
                    print("Kan station niet vinden. Check spelling")
                    continue
                bike = bigbrain.getFreeBike(station)
                if not bike:
                    print("Geen fiets in dit station, geef een ander station")
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
            station.printStationInfo(station, username)
        
