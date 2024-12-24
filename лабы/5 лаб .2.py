import math
class Circle:
    def get_perimetr(self):
        self.perimetr = 2*self.radius*math.pi
    def __init__(self, radius):
        self.radius = radius()
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
        else:
            print("radius need be positive .")
circle = Circle()
print("Current radius is:", circle.get_radius())
new_radius = float(input("Enter new radius: "))
circle.set_radius(new_radius)
print("New radius:", circle.get_radius())
#self в классах питон