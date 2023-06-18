from worldgen import Generator
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
import time
import random
import pickle
import os

class Controller:
    def __init__(self, numBikes=3620, numUsers=4200):
        self.gen = Generator(numBikes, numUsers)
        # bikes, stations, users come from the generator
        self.stations = self.gen.stations
        self.users = self.gen.users
        self.bikes = self.gen.bikes
        self.transporters = self.gen.transporters

        if not os.path.exists("./pickle.dat"):
        # vult stations met fietsen
            self.gen.fillStations(self.stations, self.bikes)

    def rentBike(self, user: Gebruiker, bike: Fiets):
        pass
    
    def getStationById(self, id): #werkt
        for el in self.stations:
            if el.id == id:
                return el
        return None

    def getStationByName(self, name): #werkt
        for el in self.stations:
            if el.name == name:
                return el
        return None
    
    def nameInUsers(self, name): #werkt
        for el in self.users:
            if el.username == name:
                return True
        return False


    def moveBike(self, station: Station, bike: Fiets):
        bike.station = station.id
        slot = station.getFreeSlot()
        slot.setBike(bike.id)
        station.addBike(bike)

    def depositBike(self,station: Station, bike: Fiets):
        bike.station = station.id
        slot = station.getFreeSlot()
        slot.setBike(bike.id)
        station.addBike(bike)

    def printAllUsers(self): #werkt
        for user in self.users:
            print(user.id)
            print(user.username)
    
    def getTotalUserCount(self): #werkt
        usernames = self.users
        # print(f"There are {len(usernames)} registered users.")
        totalUserCount = len(usernames)
        return totalUserCount
    
    def printUserInfo(self, user: Gebruiker): #werkt
        print(f"The user {user.username} has a bike: {'yes' if user.hasBike else 'no'}")

    def addUser(self, username): #werkt
        gebruiker = Gebruiker(len(self.users), username)
        self.users.append(gebruiker)
        print(f"User {username} added.")
    
    def printAvailableStations(self): #werkt
        print("The following stations have available slots:")
        for station in self.stations:
            if station.hasFreeSlot() and not station.maintenance:
                print(station.name)

    def getAvailableStations(self): #werkt
        availableStations = []
        for station in self.stations:
            if station.hasFreeSlot() and not station.maintenance:
                availableStations.append(station)
        return availableStations

    def askStationNumber(self): #werkt
        for i, station in enumerate(self.stations):
                    print(f"{i + 1}. {station.name}")
        station_number = int(input("Geef het nummer van het station: "))
        if station_number < 1 or station_number > len(self.stations):
            print("Ongeldig stationnummer. Probeer opnieuw.")
            return None
        station = self.stations[station_number - 1]
        return station
    
    def askAvailableStationNumber(self): #werkt
        for i, station in enumerate(self.stations):
            if station.hasFreeSlot() and not station.maintenance:
                print(f"{i + 1}. {station.name}")

        station_number = int(input("Geef het nummer van het station: "))
        if station_number < 1 or station_number > len(self.stations):
            print("Ongeldig stationnummer. Probeer opnieuw.")
            return None
        station = self.stations[station_number - 1]
        return station
    
    def askStationNumberWithBike(self): #werkt
        for i, station in enumerate(self.stations):
            if station.hasBike() and not station.maintenance:
                print(f"{i + 1}. {station.name}")
        
        station_number = int(input("Geef het nummer van het station: "))
        if station_number < 1 or station_number > len(self.stations):
            print("Ongeldig stationnummer. Probeer opnieuw.")
            return None
        station = self.stations[station_number - 1]
        return station

    
    def getUserId(self, username): #werkt
        for user in self.users:
            if user.username == username:
                return user.id
        user = self.addUser(username)
        return user.id
    
    def getUserByName(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def fillStations(self):
        for station in self.stations:
            station.addBike(self.bikes)

    def beginInterface(self):
        valid_responses = []
        for i in range(13):
            valid_responses.append(i)
        while True:
            print("Welkom in de stationsinterface.")
            print("Wat wil je doen?")
            print("1. fiets handmatige terminal")
            print("2. automatische simulatie")
            print("3. web html pagina exporteren")
            print("4. Exit")
            response = input("Kies een optie: ")
            try:
                response = int(response)
            except Exception as e:
                print(e)

            if response not in valid_responses:
                print("Ongeldige optie, probeer opnieuw.")
                continue

            match(response):
                case 1: #werkt
                    self.StationInterface()
                case 2: #werkt
                    self.simulatieInterface()
                case 3: 
                    self.exportHTML()
                case 4:
                    print("Tot ziens!")
                    exit()
                    

                

    def StationInterface(self):
        username = input("Geef gebruiksernaam ")
        if self.nameInUsers(username):
            print(f"Welkom terug {username}")
        else:
            self.addUser(username)

        user = self.getUserByName(username)

        valid_responses = []
        for i in range(13):
            valid_responses.append(i)
        while True:
            print("Welkom in de stationsinterface.")
            print("Wat wil je doen?")
            print("1. fiets huren")
            print("2. fiets terugbrengen")
            print("3. Station informatie")
            print("4. Gebruiker informatie")
            print("5. Toon alle beschikbare stations")
            print("6. exporteer info als web pagina")
            print("7. Exit en sla op")
            response = input("Kies een optie: ")
            try:
                response = int(response)
            except Exception as e:
                print(e)

            if response not in valid_responses:
                print("Ongeldige optie, probeer opnieuw.")
                continue

            match(response):
                case 1: #werkt
                    # fiets lenen
                    if user.hasBike:
                        print("Je hebt al een fiets.")
                        continue
                    station = self.askStationNumberWithBike()
                    if not station:
                        print("Kan station niet vinden. Check spelling")
                        continue
                    user.takeBike(station)


                case 2: #werkt
                    # fiets terugbrengen
                    if not user.hasBike:
                        print("Je hebt geen fiets om terug te brengen.")
                        continue
                    station = self.askStationNumber()
                    if not station:
                        print("Kan station niet vinden. Check spelling")
                        continue
                    user.returnBike(station)

                case 3:
                    station = self.askStationNumber()
                    if not station:
                        print("Kan station niet vinden. Check spelling")
                        continue
                    station.printStationInfo()
                    input("Druk op enter")

                case 4:
                    user.printUserInfo()
                    input("Druk op enter")
                
                case 5:
                    self.printAvailableStations()
                    input("Druk op enter")

                case 7:
                    data = [self.users, self.bikes, self.stations, self.transporters]
                    with open("pickle.dat", 'wb') as f:
                        pickle.dump(data, f)
                    print("Tot ziens!")
                    break

    def simulatieInterface(self):
        valid_responses = []
        for i in range(5):
            valid_responses.append(i)
        while True:
            print("Welkom in de simulatieinterface.")
            print("Wat is de snelheid van de simulatie?")
            print("1. 0.5x")
            print("2. 1x")
            print("3. 10x")
            print("4. 100x")

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
                    self.simSpeed = 0.5
                    self.sim(self.simSpeed)
                case 2:
                    self.simSpeed = 1
                    self.sim(self.simSpeed)
                case 3: 
                    self.simSpeed = 10
                    self.sim(self.simSpeed)
                case 4:
                    self.simSpeed = 100
                    self.sim(self.simSpeed)
            break
                
    def simUser(self, user): #werkt
        if not user.hasBike:
            station = random.choice(self.getAvailableStations())
            if not station:
                print("Kan station niet vinden. Check spelling")
                return
            user.takeBike(station)
        else:
            station = random.choice(self.stations)
            if not station:
                print("Kan station niet vinden. Check spelling")
                return
            user.returnBike(station)

    def simTransporter(self, transporter): #werkt
        if  not transporter.hasBike:
            transporter.startBikePickup(self.stations)
        else:
            transporter.startBikeDropoff(self.stations)

    def sim(self, simSpeed): #werkt
        try:
            while True:
                choices = [1, 2]
                choice = random.choice(choices)
                user = random.choice(self.users)
                transporter = random.choice(self.transporters)
                match(choice):
                    case 1:
                        self.simUser(user)
                        self.simUser(user)
                    case 2:
                        self.simTransporter(transporter)
                time.sleep(1/simSpeed)

        except KeyboardInterrupt:
            print("Tot ziens!")
            data = [self.users, self.bikes, self.stations, self.transporters]
            with open("pickle.dat", 'wb') as f:
                pickle.dump(data, f)
            return

    def exportHTML(self):
        pass
            



