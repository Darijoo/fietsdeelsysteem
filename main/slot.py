class Slot: # slots in stations
    def __init__(self, slot_id, bike=None):
        self.slot_id = slot_id
        self.bike = bike

    def assign_bike(self, bike):
        self.bike = bike

    def remove_bike(self):
        self.bike = None