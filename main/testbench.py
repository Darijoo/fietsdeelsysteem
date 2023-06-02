from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets
from pick import pick

bigbrain = Controller()


username = input("Geef gebruiksernaam ")
if username not in bigbrain.users:
    bigbrain.addUser(username)
user = bigbrain.getUserByName(username)

user.printUserInfo()
# bigbrain.printUserInfo(user)
# bigbrain.printAllUsernames()