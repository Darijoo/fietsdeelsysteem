import gebruiker 

class Transporter(gebruiker.Gebruiker): # fietsen verplaatsen
    def __init__(self, gebruikers_id, name):
        super().__init__(gebruikers_id, name)
        self.transport_geschiedenis = []

    def transport_fiets(self, fiets, bron_station, bestemming_station):
        source_slot = bron_station.slots[fiets.slot_id]
        destination_slot = bestemming_station.slots[fiets.slot_id]

        source_slot.verwijder_fiets()
        destination_slot.assign_fiets(fiets)

        self.transport_geschiedenis.append({
            "bike_id": fiets.fiets_id,
            "source_station_id": bron_station.station_id,
            "destination_station_id": bestemming_station.station_id
        })
