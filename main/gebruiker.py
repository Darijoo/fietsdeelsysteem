class Gebruiker:
    def __init__(self, id, usernames):
        self.usernames = usernames # gebruikersnaam
        self.id = id
        self.heeftFiets = False

    def getAllUsers(self, usernames):
        for user in usernames:
            print(user.usernames)

    def getTotalUserCount(self, usernames):
        print(f"There are {len(usernames)} registered users.")

    def getUserInfo(self, usernames):
        print(f"The user {self.usernames} has a bike: {'yes' if self.hasBike else 'no'}")

    def addUser(self, usernames):
        usernames.append(self)
        print(f"The user {self.usernames} has been added.")

    def getBike(self, bike):
        if not self.hasBike:
            self.hasBike = True
            bike.inUse = True
            print(f"The user {self.usernames} now has a bike.")
        else:
            print(f"The user {self.usernames} already has a bike.")

    def returnBike(self, bike):
        if self.hasBike:
            self.hasBike = False
            bike.inUse = False
            print(f"The user {self.usernames} no longer has a bike.")
        else:
            print(f"The user {self.usernames} has no bike to return.")

