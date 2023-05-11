class Station:
    def __init__(self, station_id, name, capacity):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.slots = []
        self.transporters = []

    def add_slot(self, slot):
        self.slots.append(slot)

    def add_transporter(self, transporter):
        self.transporters.append(transporter)


class Slot:
    def __init__(self, slot_id, bike=None):
        self.slot_id = slot_id
        self.bike = bike

    def assign_bike(self, bike):
        self.bike = bike

    def remove_bike(self):
        self.bike = None


class Bike:
    def __init__(self, bike_id):
        self.bike_id = bike_id


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Transporter(User):
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


class Logger:
    def __init__(self):
        self.log = []

    def log_movement(self, bike_id, source_station_id, destination_station_id):
        self.log.append({
            "bike_id": bike_id,
            "source_station_id": source_station_id,
            "destination_station_id": destination_station_id
        })
