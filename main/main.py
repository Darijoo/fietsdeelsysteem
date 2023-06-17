# from jsonParser import stations, username
from controller import Controller
from gebruiker import Gebruiker
from station import Station
from fiets import Fiets

bigbrain = Controller()

username = input("Geef gebruiksernaam ")
if username in bigbrain.users:
    print(f"Welkom terug {username}")
else:
    bigbrain.addUser(username)
    


user = bigbrain.getUserByName(username)


bigbrain.StationInterface(user)

