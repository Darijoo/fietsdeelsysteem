import json
import classes

with open("velo.geojson", "r") as f:
    velo = json.load(f)

with open("userlist.json", "r") as f:
    userlist = json.load(f)

features = velo.get("features")

stations = []
for el in features:
    prop = el.get("properties")
    if (prop.get("Objecttype") == "VELOSTATION"):
        stations.append(classes.Station(prop.get("Naam"), prop.get("Objectcode"), prop.get("Aantal_plaatsen"), [prop.get("Type_velo")], prop.get("Gebruik")))

username = []
for user in userlist:
    username.append(classes.Gebruiker(username))


