y = int(input('Введите скорость мотоциклиста: '))
x = int(input('Введите время в пути: '))
z = x*y
b = z/109
if z <= 109:
    a = 109 - z
    print(a)
else:
    c = round((b - int(b))*109)
    print(c)