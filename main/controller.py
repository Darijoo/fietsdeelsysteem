from worldgen import Generator
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from slot  import Slot

class Controller:
    def __init__(self):
        self.gen = Generator(30, 100)
        # fietsen, stations, gebruikers komen van generator

        station = self.gen.getStations()[0]
        print(station.name)
        for el in self.gen.getBikes()[:10]:
            station.voegFietsToe(el)


    def rentBike(self, user: Gebruiker, bike: Fiets):
        pass

    def getStationByID(self, id):
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
        for fiets in station.fietsen:
            if not fiets.in_gebruik:
                return fiets
        return None

    def verplaatsFiets(self, station: Station, fiets: Fiets):
        fiets.station = station.id
        slot = station.getFreeSlot()
        slot.setFiets(fiets.id)
        station.voegFietsToe(fiets)

