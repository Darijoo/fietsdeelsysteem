import gebruiker 

class Transporter(gebruiker.Gebruiker): # fietsen verplaatsen
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.transport_history = []

    def transport_bike(self, bike, source_station, destination_station):
        source_slot = source_station.slots[bike.slot_id]
        destination_slot = destination_station.slots[bike.slot_id]

        source_slot.remove_bike()
        destination_slot.assign_bike(bike)

        self.transport_history.append({
            "bike_id": bike.bike_id,
            "source_station_id": source_station.station_id,
            "destination_station_id": destination_station.station_id
        })
