class Gebruiker():
    def __init__(self,id, username):
        self.username = username # gebruikersnaam
        self.id = id # gebruikers id
        self.hasBike = False # heeft de gebruiker een fiets?

    def printUserInfo(self, id, username, hasBike):
        print(f"User ID: {id}")
        print(f"Username: {username}")
        print("Has a bike" if hasBike else "Does not have a bike")

    def getBike(self, bike):
        if not self.hasBike:
            self.hasBike = True
            bike.inUse = True
            print(f"The user {self.username} now has a bike.")
        else:
            print(f"The user {self.username} already has a bike.")

    def returnBike(self, bike):
        if self.hasBike:
            self.hasBike = False
            bike.inUse = False
            print(f"The user {self.username} no longer has a bike.")
        else:
            print(f"The user {self.username} has no bike to return.")

