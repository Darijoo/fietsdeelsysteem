import random
import json
class World:
    # Aantal fietsen en gebruikers
    num_bikes = 4200
    num_users = 1000
    def __init__(self, num_bikes, num_users):
        self.bikes = self.genBikes(self.num_bikes)
        self.users = self.genUsers(self.num_users)

    def genBikes(self, num_bikes):
        # Creëer een lijst van fietsen
        bikes = []
        for i in range(1, num_bikes + 1):
            bike_id = f"fiets_{i}"
            bike = {"bike_id": bike_id}
            bikes.append(bike)
        with open('bikelist.json', 'w') as outfile:
            json.dump(bikes, outfile)
        return bikes
    
    def genUsers(self, num_users):
        # lijsten met voornamen en achternamen
        voornamen = ['Dario', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Lucas', 'Mia', 'Mason', 'Jos', 'Frederik', 'Emma', 'Liam', 'Lucas', 'Mila', 'Noah', 'Finn', 'Lena', 'Louis', 'Anna', 'Julie', 'Seppe', 'Jasper', 'Lore', 'Eva', 'Lars', 'Eline', 'Thomas', 'Arthur', 'Ella', 'Vic', 'Marie', 'Alexander', 'Lina', 'Tomas', 'Jana', 'Lowie', 'Roos', 'Ruben', 'Mats', 'Fien', 'Brent', 'Julie', 'Lars', 'Nina', 'Jonas', 'Stien', 'Bram', 'Amber', 'Simon', 'Elise', 'Pieter', 'Anouk', 'Janne', 'Lotte', 'Mathis', 'Jef', 'Lien', 'Wout', 'Liv', 'Warre', 'Merel', 'Kobe', 'Louise', 'Lotte', 'Niels', 'Jolien', 'Arne', 'Laura', 'Siebe', 'Britt', 'Matthias', 'Silke', 'Oscar', 'Evy', 'Nathan', 'Lise', 'Lennert', 'Sofie', 'Nore', 'Lore', 'Maxim', 'Jolien', 'Sam', 'Céline', 'Tibo', 'Lara', 'Michiel', 'Lize', 'Vince', 'Jade', 'Bram', 'Emma', 'Thibault', 'Evelien', 'Veerle', 'Thibaut', 'Liesbeth', 'Lina', 'Klaas', 'Lize', 'Kyara', 'Stijn', 'Lieselot', 'Lorenzo', 'Bieke', 'Tine', 'Luka', 'Annelies', 'Hanne', 'Jolien', 'Joppe', 'Charlotte', 'Lieselotte', 'Cédric', 'Evy', 'Kyara', 'Jente', 'Lien', 'Emiel', 'Nina', 'Xander', 'Lara', 'Cato', 'Lars', 'Sanne', 'Sander', 'Sara', 'Jelle', 'Lana', 'Maarten', 'Mare', 'Daan', 'Elien', 'Lenn', 'Lien', 'Kjell', 'Lente', 'Rune', 'Lynn', 'Matteo', 'Louise', 'Nele', 'Jules', 'Marthe', 'Mohammed', 'Lars', 'Elien', 'Margo', 'Brecht', 'Nora', 'Yana', 'Lies', 'Nore', 'Ruben', 'Jolien', 'Iben', 'Lien', 'Jef', 'Yentl', 'Lina', 'Ferre', 'Lina', 'Joke', 'Lieselot', 'Astrid', 'Yentl', 'Lotte', 'Jules', 'Stefanie', 'Joppe', 'Lotte', 'Elias', 'Hanne', 'Lucca', 'Lena', 'Femke', 'Rune', 'Lena']
        achternamen = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Dubois', 'Lambert', 'Moureau', 'Lemaire', 'Simon', 'Janssens', 'Noël', 'Dumont', 'Dupont', 'Jacobs', 'Michaux', 'Lefebvre', 'Collignon', 'Gilles', 'Bastin', 'Dumont', 'Leroy', 'Lemaître', 'Mathieu', 'Lambert', 'Simon', 'Dubois', 'Durant', 'Moulin', 'Henry', 'Lambert', 'Lenaerts', 'Vandenberghe', 'Fournier', 'Denis', 'François', 'Jacques', 'Martin', 'Léonard', 'Leroy', 'Benoît', 'Dubois', 'Maréchal', 'Fontaine', 'Gosselin', 'Lejeune', 'Maes', 'Delvaux', 'Thiry', 'Renard', 'Bastin', 'Vandervorst', 'Van Laethem', 'Rousseau', 'Simon', 'Timmermans', 'Claes', 'Smet', 'Delvaux', 'Fernandez', 'Gérard', 'Vandenberghe', 'Moreau', 'Dujardin', 'Lambert', 'Leclercq', 'Godefroid', 'Mertens', 'Dumont', 'Vanderlinden', 'Bertrand', 'Carlier', 'Demeyer', 'Dewit', 'Dubois', 'Fernandez', 'François', 'Lefèvre', 'Lejeune', 'Lemmens', 'Lenaerts', 'Lepage', 'Maes', 'Mathieu', 'Matthys', 'Michel', 'Mouton', 'Noël', 'Pierre', 'Pierlot', 'Renard', 'Rochefort', 'Schmitz', 'Smet', 'Stevens', 'Thibaut', 'Van Bever', 'Van Damme', 'Van Laethem', 'Vandenberghe', 'Vanderlinden', 'Vanderveken', 'Vansteenkiste', 'Verhaegen', 'Willems', 'Hantson', 'Seniow', 'Belluci', 'Khalifa', 'Cools', 'Verreydt']
        # lijst om namen op te slaan
        users = []
        # 1000 namen genereren
        for i in range(num_users):
            user_id = f"user_{i}"
            # Kies een willekeurige voornaam en achternaam voor de gebruiker
            voornaam = random.choice(voornamen)
            achternaam = random.choice(achternamen)
            # Voeg hier eventueel extra attributen toe aan de gebruikersobjecten
            user = {"user_id": user_id, "username": voornaam + " " + achternaam}
            users.append(user)
        # lijst met gebruikers in jsonfile dumpen
        with open('userlist.json', 'w') as outfile:
            json.dump(users, outfile)
            return users

world = World(World.num_bikes, World.num_users)
