PASS = input('Придумайте пароль. Он должен быть больше 8 символов и содержать как строчные так и заглавные буквы: ')
if len(PASS) > 8 and not PASS.isupper() and not PASS.islower() and not PASS.isdigit():
	print('Веден корректный пароль')
else:
	condition = 'Пароль не соответствует критериям'
	while condition:
		PASS = input('Пароль не соответствует критериям. Повторите ввод: ')
		if len(PASS) > 8 and not PASS.isupper() and not PASS.islower() and not PASS.isdigit():
			print('Веден корректный пароль')
			break