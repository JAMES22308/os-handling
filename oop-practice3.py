class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age}"
    
class Aircraft:
    def __init__(self, type, max):
        self.type = type
        self.max = max
        self.all_passengers = []

    def add(self, name, age):
        passenger = Passenger(name, age)
        self.all_passengers.append(passenger)

    def __str__(self):
        msg = ""
        for passenger in self.all_passengers:
            msg += f"{passenger}\n"
        return msg
    

plane = Aircraft('plane', 5)
plane.add('james', 22)
plane.add('james', 28)
print(plane)
        