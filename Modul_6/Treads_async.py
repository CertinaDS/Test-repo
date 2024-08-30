import time
import asyncio
import aiohttp

start_time = time.time()

async def get_html(link):
	print(f'Start: {link}')
	async with aiohttp.ClientSession() as session:
		async with session.get(link) as response:
			data = await response.text()
			print(len(data))

links = [
	'https://habr.com',
	'https://ya.ru',
	'https://ru.wikipedia.org',
	'https://www.google.ru',
	'https://github.com/CertinaDS/Test-repo'
]

async def main():
	tasks = [get_html(link) for link in links]
	await asyncio.gather(*tasks)
asyncio.run(main())

delta = time.time() - start_time
print(f'Время выполнения: {delta}')