import random
var = ['0', '1' ,'2']
v = random.choice(var)
a = v
v = random.choice(var)
b =v
v = random.choice(var)
c = v
if a == b == c:
	print('Совпадающих чисел 3')
elif a == b or a == c or b ==c:
	print('Совпадающих чисел 2')
else:
	print('Совпадающих чисел 0')