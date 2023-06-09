import json

class Logger: # loggen van bewegingen
    def __init__(self, file):
        self.file = file
        self.logList = []
        

    def dumpData(self):
        with open(self.file, "w") as file1:
            json.dump(self.logList, file1)

    def printData(self):
        print(self.logList)

    def logTakeBikes(self, transporter, station):
        self.logList.append({"action" : "takeBikes", "transporter" : transporter.id, "station" : station.id})
    
    def logReturnBikes(self, transporter, station):
        self.logList.append({"action" : "returnBikes", "transporter" : transporter.id, "station" : station.id})
    
    def logTakeBike(self, user, station):
        self.logList.append({"action" : "takeBike", "user" : user.id, "station" : station.id})
    
    def logReturnBike(self, user, station):
        self.logList.append({"action" : "returnBike", "user" : user.id, "station" : station.id})
        