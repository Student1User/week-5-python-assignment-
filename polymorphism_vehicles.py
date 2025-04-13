# Base class for vehicles
class Vehicle:
    def move(self):
        pass  # A generic move method (can be overridden)

# Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Demonstrating polymorphism
def vehicle_move(vehicle):
    vehicle.move()

# Creating instances of Car and Plane
my_car = Car()
my_plane = Plane()

# Calling the move method on both objects
vehicle_move(my_car)    # Output: Driving 🚗
vehicle_move(my_plane)  # Output: Flying ✈️
