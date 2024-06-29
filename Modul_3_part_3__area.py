A = float(input('Длина стороны A: '))
B = float(input('Длина стороны B: '))
C = float(input('Длина стороны C: '))
def area():
    S = (A + B + C) / 2
    Area = (S * (S - A) * (S - B) * (S - C)) ** 0.5
    print('Площадь треугольника равна:', round(Area, 2))
area()