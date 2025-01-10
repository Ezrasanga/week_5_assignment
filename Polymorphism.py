class Vehicle:
    def move(self):
        """
        Generic move method for a vehicle.
        """
        print("The vehicle is moving.")

class Car(Vehicle):
    def move(self):
        """
        Specific move method for a car.
        """
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        """
        Specific move method for a plane.
        """
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        """
        Specific move method for a boat.
        """
        print("Sailing 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
