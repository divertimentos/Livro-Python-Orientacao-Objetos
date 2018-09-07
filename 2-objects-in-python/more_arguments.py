import math


class Point:
    def move(self, x, y):  # The move method accepts two arguments, x and y,

        self.x = x  # And sets the values on the self object
        self.y = y
    
    def reset(self):
        self.move(0, 0)

    '''
    Reset calls move, since a reset is just a move
    to a specific known location.
    '''
    
    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y) ** 2
        )

# How to use it:

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)

print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))
