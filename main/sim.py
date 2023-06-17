import random
import time

class modes():
    def __init__(self, stations, users, bikes, transporters):
        self.stations = stations
        self.users = users
        self.bikes = bikes

    def simulation(self):
        userType = ["gebruiker", "gebruiker", "gebruiker", "gebruiker", "gebruiker", "gebruiker", "transporteur",
                 "transporteur"]
        opdracht_type = ["plaats", "leen"]
        if restart:
            try:
                while True:
                    person = random.choice(userType)
                    opdracht = random.choice(opdracht_type)
                    handeling_set = set()
                    handeling_set.add(person)
                    handeling_set.add(opdracht)
                    if handeling_set == {"gebruiker", "plaats"}:
                        current_user = random.choice(users)
                        current_user.takeBike(random.choice(self.stations))
                    elif handeling_set == {"gebruiker", "leen"}:
                        current_user = random.choice(users)
                        current_user.returnBike(random.choice(self.stations))
                    elif handeling_set == {"transporteur", "plaats"}:
                        current_user = random.choice(transporters)
                        current_user.plaats_fietsen(random.choice(stations), random.randint(1, 20))
                    elif handeling_set == {"transporteur", "leen"}:
                        current_user = random.choice(transporters)
                        current_user.neem_fietsen(random.choice(stations), random.randint(1, 20))
                    time.sleep(0.5)
            except KeyboardInterrupt:
                data = [users, transporters, stations]
                with open("pickle.dat", 'wb') as f:
                    pickle.dump(data, f)
                log.dump_data()
                main()
        else:
            users = users_par
            transporters = transporters_par
            try:
                while True:
                    person = random.choice(userType)
                    opdracht = random.choice(opdracht_type)
                    handeling_set = set()
                    handeling_set.add(person)
                    handeling_set.add(opdracht)
                    if handeling_set == {"gebruiker", "plaats"}:
                        current_user = random.choice(users)
                        current_user.neem_fiets(random.choice(stations))
                    elif handeling_set == {"gebruiker", "leen"}:
                        current_user = random.choice(users)
                        current_user.plaats_fiets(random.choice(stations))
                    elif handeling_set == {"transporteur", "plaats"}:
                        current_user = random.choice(transporters)
                        current_user.plaats_fietsen(random.choice(stations), random.randint(1, 20))
                    elif handeling_set == {"transporteur", "leen"}:
                        current_user = random.choice(transporters)
                        current_user.neem_fietsen(random.choice(stations), random.randint(1, 20))
                    time.sleep(0.5)
            except KeyboardInterrupt:
                data = [users, transporters, stations]
                with open("pickle.dat", 'wb') as f:
                    pickle.dump(data, f)
                log.dump_data()
                main()