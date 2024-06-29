import json
LogPass = {
}
L = input('Придумайтете логин: ')
P = input('Придумайтете пароль: ')
LogPass['login'] = L
LogPass['password'] = P
def register(LogPass):
	with open("LogPass.json", "w") as file:
		json.dump(LogPass, file)
register(LogPass)

