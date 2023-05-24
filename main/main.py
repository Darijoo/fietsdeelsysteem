# from jsonParser import stations, username
from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets

bigbrain = Controller()

# station = Station("Example Station", "123", 10,"In gebruik")
# station.printSystemInfo(stations, username)

# valid_responses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
valid_responses = []
for i in range(13):
    valid_responses.append(i)

username = input("Geef gebruiksernaam")

while True:
    print("Wat wil je doen?")
    print("1. Fiets huren")
    print("2. Fiets terugbrengen")
    print("8. Station informatie")
    print("11. Gebruiker informatie")
    print("12. Toon alle beschikbare stations")
    print("13. Exit")
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
            fiets = None
            while(not fiets):
                station = bigbrain.getStationByName(input("geef naam van station: "))
                if not station:
                    print("Kan station niet vinden. Check spelling")
                    continue
                fiets = bigbrain.getFreeBike(station)
                if not fiets:
                    print("Geen fiets in dit station, geef een ander station")
                    continue

if response == '12':
    station.toonVrijeStations(stations)
