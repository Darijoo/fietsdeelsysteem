import json
import station
import gebruiker

with open("velo.geojson", "r") as f:
    velo = json.load(f)

with open("userlist.json", "r") as f:
    userlist = json.load(f)

features = velo.get("features")

stations = []
for el in features:
    prop = el.get("properties")
    if (prop.get("Objecttype") == "VELOSTATION"):
        stations.append(station.Station(prop.get("Naam"), prop.get("Objectcode"), prop.get("Aantal_plaatsen"), prop.get("Gebruik")))

username = []
for user in userlist:
    username.append(gebruiker.Gebruiker(username))


