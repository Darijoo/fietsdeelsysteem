from worldgen import Generator
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from slot import Slot

class Controller:
    def __init__(self, numBikes, numUsers):
        self.gen = Generator(numBikes, numUsers)
        # bikes, stations, users come from the generator

        station = self.gen.getStations()
        # print(station.name)
        
        for el in self.gen.getBikes():
            for station in self.gen.getStations():
                if station.id == el.station:
                    station.addBike(el)

    def rentBike(self, user: Gebruiker, bike: Fiets):
        pass

    def getStationById(self, id):
        for el in self.gen.getStations():
            if el.id == id:
                return el
        return None

    def getStationByName(self, name):
        for el in self.gen.getStations():
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

    def printAllUsernames(self):
        for user in self.gen.getUsers():
            print(user.id)
            print(user.username)
    
    def getTotalUserCount(self):
        usernames = self.gen.getUsers()
        # print(f"There are {len(usernames)} registered users.")
        totalUserCount = len(usernames)
        return totalUserCount
    
    def printUserInfo(self):
        print(f"The user {self.username} has a bike: {'yes' if self.hasBike else 'no'}")

    def addUser(self, username):
        self.users.append(username)
        print(f"User {username} added.")