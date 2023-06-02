from worldgen import Generator
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from slot import Slot

class Controller:
    def __init__(self, numBikes=3620, numUsers=4200):
        self.gen = Generator(numBikes, numUsers)
        # bikes, stations, users come from the generator
        self.stations = self.gen.getStations()
        self.users = self.gen.getUsers()
        self.bikes = self.gen.getBikes()
        
        for el in self.gen.getBikes():
            for station in self.gen.getStations():
                if station.id == el.station:
                    station.addBike(el)

    def rentBike(self, user: Gebruiker, bike: Fiets):
        pass
    
    def getStationById(self, id):
        for el in self.stations:
            if el.id == id:
                return el
        return None

    def getStationByName(self, name): #werkt
        for el in self.stations:
            if el.name == name:
                return el
        return None

    def getFreeBike(self, station: Station):
        for bike in station.bikes:
            if not bike.inUse:
                return bike
        return None

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
    
    def printUserInfo(self, user: Gebruiker): 
        print(f"The user {user.username} has a bike: {'yes' if user.hasBike else 'no'}")

    def addUser(self, username): #werkt
        gebruiker = Gebruiker(len(self.users), username)
        self.users.append(gebruiker)
        print(f"User {username} added.")
    
    def printAvailableStations(self): #werkt
        print("The following stations have available slots:")
        for station in self.gen.getStations():
            if len(station.bikes) < station.capacity and not station.maintenance:
                print(station.name)

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
            if len(station.bikes) < station.capacity and not station.maintenance:
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