class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)
p1 = Point(2, -2)
p1.distance()
