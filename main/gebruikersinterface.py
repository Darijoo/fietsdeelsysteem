from jsonParser import stations, username
from classes import Station

station = Station("Example Station", "123", 10, ["type1", "type2"], "In gebruik")
station.printSystemInfo(stations, username)

valid_responses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
while True:
    print("Wat wil je doen?")
    print("1. Fiets huren")
    print("2. Fiets terugbrengen")
    print("3. Fiets verplaatsen")
    print("4. Fiets verwijderen")
    print("5. Station toevoegen")
    print("6. Station verwijderen")
    print("7. Station onderhoud")
    print("8. Station informatie")
    print("9. Gebruiker toevoegen")
    print("10. Gebruiker verwijderen")
    print("11. Gebruiker informatie")
    print("12. Toon alle beschikbare stations")
    print("13. Exit")
    response = input("Kies een optie: ")

    if response not in valid_responses:
        print("Ongeldige optie, probeer opnieuw.")
        continue
    else:
        break
    
if response == '12':
    station.toonVrijeStations(stations)
