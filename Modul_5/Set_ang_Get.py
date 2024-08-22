class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self):
        return (self. x**2 + self.y**2)**(1/2)
        print
p1 = Point(10,-5)
print(f'Расстояние между координатами {p1.distance()}')