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