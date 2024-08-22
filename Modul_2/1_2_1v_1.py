number_1 = int(input('Ведите число: '))
number_2 = int(input('Ведите число: '))
number_3 = int(input('Ведите число: '))
if number_1 == number_2 == number_3:
	print('Совпадающих чисел 3')
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
	print('Совпадающих чисел 2')
else: 
	print('Совпадающих чисел 0')