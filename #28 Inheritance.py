# Inheritance is a mechanism for reusing code
# in programming there is a principle called "dry" it means dont repeat your self

class Vehicle():
    def get_colour(self, colour):
        print(f"colour is {colour}")

    def get_gas_status(self, gas):
        print(f"gas level is {gas}")

    def get_speed(self, speed):
        print(f"speed is {speed}")


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def weight(weight):
        print(f"weight is {weight}")


class UserInput():
    colour = input("what is the colour of your vehicle")
#truck1 = truck()
