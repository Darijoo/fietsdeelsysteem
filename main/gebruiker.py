class Gebruiker:
    def __init__(self, id, username):
        self.username = username # gebruikersnaam
        self.id = id
        self.heeftFiets = False

    def geefAlleGebruikers(self, username):
        for user in username:
            print(user.username)

    def geefTotaalAantalGebruikers(self, username):
        print(f"Er zijn {len(username)} gebruikers geregistreerd.")

    def geefGebruikerInfo(self, username):
        print(f"De gebruiker {self.username} heeft een fiets: {'ja' if self.heeftFiets else 'nee'}")

    def voegGebruikerToe(self, username):
        username.append(self)
        print(f"De gebruiker {self.username} is toegevoegd.")

    def geefFiets(self, fiets):
        if self.heeftFiets == False:
            self.heeftFiets = True
            fiets.in_gebruik = True
            print(f"De gebruiker {self.username} heeft nu een fiets.")
        else: 
            print(f"De gebruiker {self.username} heeft al een fiets.")

    def returnFiets(self, fiets):
        if self.heeftFiets == True:
            self.heeftFiets = False
            fiets.in_gebruik = False
            print(f"De gebruiker {self.username} heeft nu geen fiets meer.")
        else:
            print(f"De gebruiker {self.username} heeft geen fiets om in te leveren.")
