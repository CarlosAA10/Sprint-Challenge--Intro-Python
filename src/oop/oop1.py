# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    def __init__(self):
        pass # this is the base class

class FlightVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass # this extends vehicle

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        pass # this class extends vehicle

class Starship(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass # this class extends flightVehicle

class AirPlane(FlightVehicle):
    def __init__(self):
        super().__init__()
        pass # this class extends FlightVehicle

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass # this class extends groundVehicle

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
        pass 
