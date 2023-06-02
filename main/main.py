# from jsonParser import stations, username
from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets

bigbrain = Controller()

username = input("Geef gebruiksernaam ")
if username not in bigbrain.users:
    bigbrain.addUser(username)

user = bigbrain.getUserByName(username)


valid_responses = []
for i in range(13):
    valid_responses.append(i)

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
                station = bigbrain.askStationNumber()
                bike = bigbrain.getFreeBike(station)
                if not bike:
                    print("Geen fiets in dit station. Kies een ander station.")
                    continue

        case 2:
            bike = None
            if not bike:
                print("Geen fiets in dit station. Kies een ander station.")
            while(bike):
                station = bigbrain.askAvailableStationNumber()
                if not station:
                    print("Kan station niet vinden. Check spelling")
                    continue
                bike = bigbrain.getFreeBike(station)
                if not bike:
                    print("Geen fiets in dit station, geef een ander station")
                    continue
        case 3:
            station = bigbrain.askAvailableStationNumber()
            if not station:
                print("Kan station niet vinden. Check spelling")
                continue
            station.printStationInfo()
            input("Druk op enter")

        case 4:
            user.printUserInfo()
            input("Druk op enter")
        
        case 5:
            bigbrain.printAvailableStations()
            input("Druk op enter")

        case 7:
            print("Tot ziens!")
            break