class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def start_engine(self):
        print("The vehicle's engine is starting...")

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        print("The car's engine is starting...")

    def drive(self):
        print("The car is being driven...")


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        print("The truck's engine is starting...")

    def haul(self):
        print("The truck is hauling...")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("The motorcycle's engine is starting...")

    def ride(self):
        print("The motorcycle is being ridden...")

vehicle = Vehicle('bmw', 'm5', 2018, 1900)
print(vehicle.start_engine())

car = Car('bmw', 'm5', 2018, 1900, 4, 5)
print(car.start_engine())
print(car.drive())

truck = Truck('man', 'tgx', 2008, 8000, 10000, 30000)
print(truck.start_engine())
print(truck.haul())

motorcycle = Motorcycle('kawasaki', 'h2r', 2021, 216, 2, False)
print(motorcycle.start_engine())
print(motorcycle.ride())
