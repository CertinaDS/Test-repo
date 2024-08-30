import time
from threading import Thread
import requests
start_time = time.time()
def get_html(link):
	print(f'Start: {link}')
	with requests.get(link) as response:
		data = response.text
		print(len(data))

links = [
	'https://habr.com',
	'https://ya.ru',
	'https://ru.wikipedia.org',
	'https://www.google.ru',
	'https://github.com/CertinaDS/Test-repo'
]
threads = [Thread(target=get_html(link), args=(link, )) for link in links]
for t in threads:
	t.start()
for t in threads:
	t.join()
delta = time.time() - start_time
print(f'Время выполнения: {delta}')

