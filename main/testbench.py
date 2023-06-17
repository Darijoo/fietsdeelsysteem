from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets

bigbrain = Controller()

bigbrain.gen.fillStations(bigbrain.stations, bigbrain.bikes)

# station = bigbrain.askStationNumber()

# station.printStationInfo(station)

bigbrain.printAvailableStations()