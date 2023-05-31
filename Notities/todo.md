Essentieel:

- Objecten: fiets-stations, slots (ook plaatsen genoemd), fietsen, gebruikers, fietstransporteurs, loggen van gebruik
  {
  -Stations bevatten een aantal plaatsen of slots, fietsen kunnen gekoppeld zijn aan een slot enz...
  -Fietstransporteurs zijn de vrachtwagens die rondrijden door de stad en in bulk fietsen verdelen van volle stations naar legere stations.
  -Je modelleert ze als een bijzondere soort gebruikers.
  -Je logt alle verplaatsingen en houdt ze bij in objecten die je via compositie bindt aan de juiste objecten.
  }

- Eerste start van de toepassing
  {
  -Maak aan de hand van JSON-dataset een reële situatie (bv: 4200 fietsen, 309 stations en +55000 gebruikers)
  -Set aanvullen met eigen data
  -Naamgenerator voor gebruikers //zie namengen.py
  }

- Data opslaan en bijhouden in bestand(en)
  {
  -Start je de toepassing opnieuw dan geef je de keuze om opnieuw te beginnen of om verder te gaan vanaf de bestaande situatie.
  -De interface is de terminal.
  -Je zorgt er voor dat er relatief gebruiksvriendelijk met de
  toepassing kan worden omgesprongen door gebruik van een menu.
  }

- Acties die manueel moeten kunnen geïnitieerd worden zijn het ontlenen van (een) fiets(en), het terug
  inchecken van (een) fiets(en) voor zowel gebruikers als transporteurs.

- Aanmaken HTML-output
  {
  -Moet je kunnen initieren vanuit interface.
  -Je genereert een verzameling van webpaginaʼs waarin je de toestand kan opvragen per station of per gebruiker en per fiets
  -Statische website generator in de folder \_site
  -CSS voor gebruiksvriendelijkheid
  }

- Simulatiemodus
  {
  -Tijd versnellen
  -Registreren van verplaatsingen doorheen de stad kan automatiseren
  -Kan gestart worden vanuit terminal-interface
  -Kan ook gestart worden door de applicatie te starten met het -s argument
  }

- Gebruikersinterface
  {

}

- dingen dat meneer zegt
  {
  -Oplossing filmzalen zeker bekijken
  -Geen id gaan gerbuiken slots een object gebruiken
  -Slots wel identifier gebruiken
  -Output html
  -En picklen ook in menu
  -Pythonanyware
  }

stappenplan interface:

1. Gebruiker geeft naam in (als de gebruiker nog niet bestaat dan wordt er een nieuwe gebruiker aangemaakt en in de lijst van gebruikers gestoken)
2. Dan krijgt de gebruiker een keuzemenu te zien en moet hij een optie kiezen van wat hij wilt doen
3. Als hij 1 kiest betekent dat hij een fiets wilt huren. Dan kiest hij eerst uit welk station hij een fiets wilt huren. Daarna krijgt hij een fiets. (Als er geen fiets in het gekozen station zit moet hij een andere kiezen)
4. Als hij 2 kiest dan wilt hij een fiets terugbrengen. (Als de gebruiker al een fiets heeft krijgt hij een melding dat hij maar 1 fiets kan hebben en gaat hij terug naar het keuzemenu) Dan gaat hij een station moeten kiezen waar hij het wilt inleveren. Dan krijgt hij een melding dat de fiets is ingeleverd en heeft de gebruiker geen fiets meer.
5. Als hij 3 kiest dan vraagt hij informatie over een station. Hij kiest eerst een station. Dan krijgt hij alle info over het gekozen station. En na input van de gebruiker gaat hij terug naar het menu.
6. Als hij 4 kiest krijgt hij info over zichzelf. Na input gaat de gebruiker terug naar het menu
7. Als de gebruiker op 5 drukt krijgt hij een lijst van alle beschikbare stations.
8. Als hij op 6 drukt wordt alle info gexporteerd naar een web pagina.
9. Als hij op 7 drukt gaat hij uit de interface.
