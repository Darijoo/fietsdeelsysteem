from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets

bigbrain = Controller()

for user in bigbrain.users:
    print(user.username)

# station = bigbrain.askStationNumber()

# station.printStationInfo(station)

# bigbrain.printAvailableStations()