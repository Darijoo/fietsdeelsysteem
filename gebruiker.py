class Gebruiker():
    def __init__(self,id, username):
        self.username = username # gebruikersnaam
        self.id = id # gebruikers id
        self.hasBike = False # heeft de gebruiker een fiets?
        self.bike = None # fiets van de gebruiker

    def printUserInfo(self):
        print(f"User ID: {self.id}")
        print(f"Username: {self.username}")
        print("Has a bike" if self.hasBike else "Does not have a bike")

    def getBike(self, bike):
        if not self.hasBike:
            self.hasBike = True
            bike.inUse = True
            print(f"The user {self.username} now has a bike.")
        else:
            print(f"The user {self.username} already has a bike.")

    def takeBike(self, station):
        if not self.hasBike:
            if station.hasBike():
                self.hasBike = True
                self.bike = station.withdrawBike()
                self.bike.inUse = True
                print(f"The user {self.username} now has a bike.")
            else:
                print(f"The station {station.name} has no bikes.")
        else:
            print(f"The user {self.username} already has a bike.")

    def returnBike(self, station):
        if self.hasBike:
            bike = self.bike
            station.returnBike(self.bike)
            self.hasBike = False
            self.bike.inUse = False
            self.bike = None
            print(f"The user {self.username} returned bike{bike.id}.")
        else:
            print(f"The user {self.username} has no bike to return.")

