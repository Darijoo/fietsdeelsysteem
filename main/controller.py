from worldgen import Generator
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from slot import Slot

class Controller:
    def __init__(self):
        self.gen = Generator(3620, 4200)
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