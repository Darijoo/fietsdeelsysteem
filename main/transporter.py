import gebruiker 

class Transporter(gebruiker.Gebruiker): # fietsen verplaatsen
    def __init__(self, userId, name):
        super().__init__(userId, name)
        self.transport_geschiedenis = []

    def transportBike(self, bike, sourceStation, destinationStation):
        sourceSlot = sourceStation.slots[bike.slotId]
        destinationSlot = destinationStation.slots[bike.slotId]

        sourceSlot.removeBike()
        destinationSlot.assignBike(bike)

        self.transportHistory.append({
            "bikeId": bike.bikeId,
            "sourceStationId": sourceStation.stationId,
            "destinationStationId": destinationStation.stationId
    })
