
class Logger: # loggen van bewegingen
    def __init__(self):
        self.log = []

    def log_movement(self, fiets_id, bron_station_id, bestemming_station_id):
        self.log.append({
            "fiets_id": fiets_id,
            "bron_station_id": bron_station_id,
            "bestemming_station_id": bestemming_station_id
        })