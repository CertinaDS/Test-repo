import time
import asyncio
import aiohttp

start_time = time.time()
async def get_html(link):
	print(f'Start: {link}')
	async with aiohttp.ClientSession() as request:
		async with request.get(link) as response:
			data = await response.text
			print(len(data))

links = ['https://habr.com', 'https://ya.ru', 'https://ru.wikipedia.org', 'https://www.google.ru', 'https://github.com/CertinaDS/Test-repo']

x = [get_html(link) for link in links]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(x))
delta = time.time() - start_time
print(f'Время выполнения: {delta}')