class Bus:
    def __init__(self, route, destiniation):
        self.route_number = route
        self.destination = destiniation
        self.passenger = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger)

    def pick_up(self, person):
        self.passenger.append(person)

    def drop_off(self, person):
        self.passenger.remove(person)

    def empty(self):
        self.passenger = []
    
    def pick_up_from_stop(self, bus_stop):
        for people in bus_stop.queue:
            self.passenger.append(people)
        bus_stop.clear()
        
        
