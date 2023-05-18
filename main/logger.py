
class Logger: # loggen van bewegingen
    def __init__(self):
        self.log = []

    def log_movement(self, bike_id, source_station_id, destination_station_id):
        self.log.append({
            "bike_id": bike_id,
            "source_station_id": source_station_id,
            "destination_station_id": destination_station_id
        })