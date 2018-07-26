class Vehicle:

    def __init__(self):
        print("Inside " + type(self).__name__)

    def accelerate(self):
        print("Vehicle is accelerating")

    def brake(self):
        print("Vehicle is braking")


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        print("Inside " + type(self).__name__)

    def accelerate(self):
        print("Car is accelerating")


veh = Vehicle()
car = Car()
car.accelerate()