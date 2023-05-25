
class Logger: # loggen van bewegingen
    def __init__(self):
        self.log = []
        
    def logMovement(self, bikeId, sourceStationId, destinationStationId):
        self.log.append({
            "bikeId": bikeId,
            "sourceStationId": sourceStationId,
            "destinationStationId": destinationStationId
        })
