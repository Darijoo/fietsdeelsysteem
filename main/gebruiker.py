class Gebruiker:
    def __init__(self, username):
        self.username = username # gebruikersnaam
        self.hasBike = False

    def geefAlleGebruikers(self, username):
        for user in username:
            print(user.username)

    def geefTotaalAantalGebruikers(self, username):
        print(f"Er zijn {len(username)} gebruikers geregistreerd.")

    def geefGebruikerInfo(self, username):
        print(f"De gebruiker {self.username} heeft een fiets: {'ja' if self.hasBike else 'nee'}")

    def voegGebruikerToe(self, username):
        username.append(self)
        print(f"De gebruiker {self.username} is toegevoegd.")