# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, *num_wheels):
        if len(str(num_wheels)) < 1:
           self.num_wheels = 4
        else:
            self.num_wheels = num_wheels

    def drive(self):
        return f"vroooom"
    # TODO

print(GroundVehicle(4).drive(), 'the car')

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

class Motorcycle(GroundVehicle):
    def __init__(self, *num_wheels):
        super().__init__(num_wheels)
        num_wheels = 2

    def drive(self):
        return f"BRAAAP"

print(Motorcycle(2).drive(), 'drive method in motorcycle')

# TODO

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.
for i in vehicles:
    print(f"{i.drive()} the result of printing drive on each")

# TODO
