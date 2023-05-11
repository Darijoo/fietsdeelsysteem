import random
import json

# lijsten met voornamen en achternamen
voornamen = ['Dario', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Lucas', 'Mia', 'Mason', 'Jos', 'Frederik', 'Emma', 'Liam', 'Lucas', 'Mila', 'Noah', 'Finn', 'Lena', 'Louis', 'Anna', 'Julie', 'Seppe', 'Jasper', 'Lore', 'Eva', 'Lars', 'Eline', 'Thomas', 'Arthur', 'Ella', 'Vic', 'Marie', 'Alexander', 'Lina', 'Tomas', 'Jana', 'Lowie', 'Roos', 'Ruben', 'Mats', 'Fien', 'Brent', 'Julie', 'Lars', 'Nina', 'Jonas', 'Stien', 'Bram', 'Amber', 'Simon', 'Elise', 'Pieter', 'Anouk', 'Janne', 'Lotte', 'Mathis', 'Jef', 'Lien', 'Wout', 'Liv', 'Warre', 'Merel', 'Kobe', 'Louise', 'Lotte', 'Niels', 'Jolien', 'Arne', 'Laura', 'Siebe', 'Britt', 'Matthias', 'Silke', 'Oscar', 'Evy', 'Nathan', 'Lise', 'Lennert', 'Sofie', 'Nore', 'Lore', 'Maxim', 'Jolien', 'Sam', 'Céline', 'Tibo', 'Lara', 'Michiel', 'Lize', 'Vince', 'Jade', 'Bram', 'Emma', 'Thibault', 'Evelien', 'Veerle', 'Thibaut', 'Liesbeth', 'Lina', 'Klaas', 'Lize', 'Kyara', 'Stijn', 'Lieselot', 'Lorenzo', 'Bieke', 'Tine', 'Luka', 'Annelies', 'Hanne', 'Jolien', 'Joppe', 'Charlotte', 'Lieselotte', 'Cédric', 'Evy', 'Kyara', 'Jente', 'Lien', 'Emiel', 'Nina', 'Xander', 'Lara', 'Cato', 'Lars', 'Sanne', 'Sander', 'Sara', 'Jelle', 'Lana', 'Maarten', 'Mare', 'Daan', 'Elien', 'Lenn', 'Lien', 'Kjell', 'Lente', 'Rune', 'Lynn', 'Matteo', 'Louise', 'Nele', 'Jules', 'Marthe', 'Mohammed', 'Lars', 'Elien', 'Margo', 'Brecht', 'Nora', 'Yana', 'Lies', 'Nore', 'Ruben', 'Jolien', 'Iben', 'Lien', 'Jef', 'Yentl', 'Lina', 'Ferre', 'Lina', 'Joke', 'Lieselot', 'Astrid', 'Yentl', 'Lotte', 'Jules', 'Stefanie', 'Joppe', 'Lotte', 'Elias', 'Hanne', 'Lucca', 'Lena', 'Femke', 'Rune', 'Lena']
achternamen = ['Gilles', 'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Dubois', 'Lambert', 'Moureau', 'Lemaire', 'Simon', 'Janssens', 'Noël', 'Dumont', 'Dupont', 'Jacobs', 'Michaux', 'Lefebvre', 'Collignon', 'Gilles', 'Bastin', 'Dumont', 'Leroy', 'Lemaître', 'Mathieu', 'Lambert', 'Simon', 'Dubois', 'Durant', 'Moulin', 'Henry', 'Lambert', 'Lenaerts', 'Vandenberghe', 'Fournier', 'Denis', 'François', 'Jacques', 'Martin', 'Léonard', 'Leroy', 'Benoît', 'Dubois', 'Maréchal', 'Fontaine', 'Gosselin', 'Lejeune', 'Maes', 'Delvaux', 'Thiry', 'Renard', 'Bastin', 'Vandervorst', 'Van Laethem', 'Rousseau', 'Simon', 'Timmermans', 'Claes', 'Smet', 'Delvaux', 'Fernandez', 'Gérard', 'Vandenberghe', 'Moreau', 'Dujardin', 'Lambert', 'Leclercq', 'Godefroid', 'Mertens', 'Dumont', 'Vanderlinden', 'Bertrand', 'Carlier', 'Demeyer', 'Dewit', 'Dubois', 'Fernandez', 'François', 'Lefèvre', 'Lejeune', 'Lemmens', 'Lenaerts', 'Lepage', 'Maes', 'Mathieu', 'Matthys', 'Michel', 'Mouton', 'Noël', 'Pierre', 'Pierlot', 'Renard', 'Rochefort', 'Schmitz', 'Smet', 'Stevens', 'Thibaut', 'Van Bever', 'Van Damme', 'Van Laethem', 'Vandenberghe', 'Vanderlinden', 'Vanderveken', 'Vansteenkiste', 'Verhaegen', 'Willems', 'Hantson', 'Seniow', 'Belluci', 'Khalifa', 'Cools', 'Verreydt']

# lijst om namen op te slaan
namen = []

# 1000 namen genereren
for i in range(1000):
    # willekeurige voornaam en achternaam kiezen
    voornaam = random.choice(voornamen)
    achternaam = random.choice(achternamen)
    # naam toevoegen aan lijst
    namen.append(voornaam + ' ' + achternaam)

# de namen afdrukken

with open('namen.json', 'w') as outfile:
    json.dump(namen, outfile)
