from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets

bigbrain = Controller()


# username = input("Geef gebruiksernaam ")
# if username not in bigbrain.users:
#     bigbrain.addUser(username)
# user = bigbrain.getUserByName(username)

# bigbrain.gen.fillStations(bigbrain.stations, bigbrain.bikes)

station = bigbrain.askStationNumber()

station.printStationInfo(station)

# bigbrain.printUserInfo(user)
# bigbrain.printAllUsernames()