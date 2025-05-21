class Passenger:
    """docstring"""
    def __init__(self, first_name, last_name, seat_number, ticket_type):
        self.first_name = first_name.strip().title()
        self.last_name = last_name
        self.seat_number = seat_number
        self.ticket_type = ticket_type
    def __str__(self):
        return f"{self.first_name} {self.last_name} is in seat {self.seat_number}"

class Aircraft:
    """docstring"""
    def __init__(self, aircraft_type, max_passengers):
        self.aircraft_type = aircraft_type.strip().title()
        self.max_passengers = max_passengers
        self.all_passengers = []
        
    
    def add_passenger(self, name, last_name, seat, type):
        passenger = Passenger(name, last_name, seat, type)
        self.all_passengers.append(passenger)
        return True
    def get_total_passengers(self):
        return len(self.all_passengers)

    def get_total_free_seats(self):
        return (self.max_passengers - len(self.all_passengers))

    def get_seat_availability(self, seat_number):
        if seat_number > self.max_passengers:
            return False
        for available in self.all_passengers:
            if seat_number == available.seat_number:
                return False
        return True
    def remove_passenger(self, first_name, last_name, seat_number):
        for passenger in self.all_passengers:
            if first_name == passenger.first_name:
                if last_name == passenger.last_name:
                    if seat_number == passenger.seat_number:
                        self.all_passengers.remove(passenger)
                        return True
        return False
    
    def same_name(self, name):
        count = 0
        for passenger in self.all_passengers:
            if name == passenger.first_name:
                count += 1
        if count >= 2:
            return (True, f'count: {count}')
        else:
            return False


    
        

    def __str__(self):
        msg = f"The plane contains the following passengers:\n"
        for passenger in self.all_passengers:
            msg += f"{passenger}\n"
        return msg
    
 	

small_plane = Aircraft('Cessna 182',4)
print('Adding passengers...')
small_plane.add_passenger('Paddington','Brown',2,'Business')
small_plane.add_passenger('Paddingjton','Lucy',3,'Business')
print(small_plane)
print('Adding another passenger ...')
small_plane.add_passenger('Paddinhgton','Pastuzo',4,'Business')
print(small_plane)
print('Attempt to remove Aunt Lucy but specifying the wrong seat')
small_plane.remove_passenger('Aunt','Lucy',2)

print(small_plane)
print(small_plane.same_name('Paddington'))