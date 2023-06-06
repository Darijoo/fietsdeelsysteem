import random
import json

from station import Station
from fiets import Fiets
from gebruiker import Gebruiker

class Generator:
    # Aantal fietsen en gebruikers
    # numBikes = 3620
    # numUsers = 1000
    def __init__(self, numBikes = 3620, numUsers = 4200):
        self.numBikes = numBikes 
        self.numUsers = numUsers 
        self.bikes = self.genBikes(numBikes) # Random
        self.users = self.genUsers(numUsers) # Random
        self.stations = self.genStations()    # From file

    def genBikes(self, numBikes):
        # Creëer een lijst van fietsen
        bikes = []
        for i in range(1, numBikes + 1):
            bike = Fiets(i)
            bikes.append(bike)
        # with open('bikelist.json', 'w') as outfile:
        #     json.dump(bikes, outfile)
        return bikes
    
    def genUsers(self, numUsers):
        # lijsten met voornamen en achternamen
        voornamen = ['Dario', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Lucas', 'Mia', 'Mason', 'Jos', 'Frederik', 'Emma', 'Liam', 'Lucas', 'Mila', 'Noah', 'Finn', 'Lena', 'Louis', 'Anna', 'Julie', 'Seppe', 'Jasper', 'Lore', 'Eva', 'Lars', 'Eline', 'Thomas', 'Arthur', 'Ella', 'Vic', 'Marie', 'Alexander', 'Lina', 'Tomas', 'Jana', 'Lowie', 'Roos', 'Ruben', 'Mats', 'Fien', 'Brent', 'Julie', 'Lars', 'Nina', 'Jonas', 'Stien', 'Bram', 'Amber', 'Simon', 'Elise', 'Pieter', 'Anouk', 'Janne', 'Lotte', 'Mathis', 'Jef', 'Lien', 'Wout', 'Liv', 'Warre', 'Merel', 'Kobe', 'Louise', 'Lotte', 'Niels', 'Jolien', 'Arne', 'Laura', 'Siebe', 'Britt', 'Matthias', 'Silke', 'Oscar', 'Evy', 'Nathan', 'Lise', 'Lennert', 'Sofie', 'Nore', 'Lore', 'Maxim', 'Jolien', 'Sam', 'Céline', 'Tibo', 'Lara', 'Michiel', 'Lize', 'Vince', 'Jade', 'Bram', 'Emma', 'Thibault', 'Evelien', 'Veerle', 'Thibaut', 'Liesbeth', 'Lina', 'Klaas', 'Lize', 'Kyara', 'Stijn', 'Lieselot', 'Lorenzo', 'Bieke', 'Tine', 'Luka', 'Annelies', 'Hanne', 'Jolien', 'Joppe', 'Charlotte', 'Lieselotte', 'Cédric', 'Evy', 'Kyara', 'Jente', 'Lien', 'Emiel', 'Nina', 'Xander', 'Lara', 'Cato', 'Lars', 'Sanne', 'Sander', 'Sara', 'Jelle', 'Lana', 'Maarten', 'Mare', 'Daan', 'Elien', 'Lenn', 'Lien', 'Kjell', 'Lente', 'Rune', 'Lynn', 'Matteo', 'Louise', 'Nele', 'Jules', 'Marthe', 'Mohammed', 'Lars', 'Elien', 'Margo', 'Brecht', 'Nora', 'Yana', 'Lies', 'Nore', 'Ruben', 'Jolien', 'Iben', 'Lien', 'Jef', 'Yentl', 'Lina', 'Ferre', 'Lina', 'Joke', 'Lieselot', 'Astrid', 'Yentl', 'Lotte', 'Jules', 'Stefanie', 'Joppe', 'Lotte', 'Elias', 'Hanne', 'Lucca', 'Lena', 'Femke', 'Rune', 'Lena']
        achternamen = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Dubois', 'Lambert', 'Moureau', 'Lemaire', 'Simon', 'Janssens', 'Noël', 'Dumont', 'Dupont', 'Jacobs', 'Michaux', 'Lefebvre', 'Collignon', 'Gilles', 'Bastin', 'Dumont', 'Leroy', 'Lemaître', 'Mathieu', 'Lambert', 'Simon', 'Dubois', 'Durant', 'Moulin', 'Henry', 'Lambert', 'Lenaerts', 'Vandenberghe', 'Fournier', 'Denis', 'François', 'Jacques', 'Martin', 'Léonard', 'Leroy', 'Benoît', 'Dubois', 'Maréchal', 'Fontaine', 'Gosselin', 'Lejeune', 'Maes', 'Delvaux', 'Thiry', 'Renard', 'Bastin', 'Vandervorst', 'Van Laethem', 'Rousseau', 'Simon', 'Timmermans', 'Claes', 'Smet', 'Delvaux', 'Fernandez', 'Gérard', 'Vandenberghe', 'Moreau', 'Dujardin', 'Lambert', 'Leclercq', 'Godefroid', 'Mertens', 'Dumont', 'Vanderlinden', 'Bertrand', 'Carlier', 'Demeyer', 'Dewit', 'Dubois', 'Fernandez', 'François', 'Lefèvre', 'Lejeune', 'Lemmens', 'Lenaerts', 'Lepage', 'Maes', 'Mathieu', 'Matthys', 'Michel', 'Mouton', 'Noël', 'Pierre', 'Pierlot', 'Renard', 'Rochefort', 'Schmitz', 'Smet', 'Stevens', 'Thibaut', 'Van Bever', 'Van Damme', 'Van Laethem', 'Vandenberghe', 'Vanderlinden', 'Vanderveken', 'Vansteenkiste', 'Verhaegen', 'Willems', 'Hantson', 'Seniow', 'Belluci', 'Khalifa', 'Cools', 'Verreydt']
        # lijst om namen op te slaan
        users = []
        for i in range(numUsers + 1):
            # user_id = f"user_{i}"
            # Kies een willekeurige voornaam en achternaam voor de gebruiker
            voornaam = random.choice(voornamen)
            achternaam = random.choice(achternamen)
            # Voeg hier eventueel extra attributen toe aan de gebruikersobjecten
            # user = {"user_id": user_id, "username": voornaam + " " + achternaam}
            gebruiker = Gebruiker(i, voornaam + ' ' + achternaam)
            users.append(gebruiker)
            # lijst met gebruikers in jsonfile dumpen
            # with open('userlist.json', 'w') as outfile:
            #     json.dump(users, outfile)
        return users

    def genStations(self):
        with open("velo.geojson", "r") as f:
            velo = json.load(f)
            print(json.dumps(velo, indent=4))
        features = velo.get("features")

        stations = []
        for el in features:
            prop = el.get("properties")
            if (prop.get("Objecttype") == "VELOSTATION"):
                stations.append(Station(prop.get("Naam"), prop.get("Objectcode"), prop.get("Aantal_plaatsen"), prop.get("Gebruik")))
        return stations

    def getBikes(self):
        return self.bikes

    def getUsers(self):
        return self.users

    def getStations(self):
        return self.stations
    
    def fillStations(self, stations, bikes):
        numberOfBikesSent = 0
        i = 0
        while numberOfBikesSent < self.numBikes:
            station = random.choice(stations)
            if station.hasFreeSlot():
                bike = bikes[i]
                if station.addBike(bike[i]):
                    i += 1
                    numberOfBikesSent += 1
                    bike.inUse = False