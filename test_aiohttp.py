import asyncio
import aiohttp
import time

start = time.time()
async def send_pokemon():
    async with aiohttp.ClientSession() as session:
        for i in range(1, 11):
            url = f"https://pokeapi.co/api/v2/pokemon/{i}"
            async with session.get(url) as response:
                pokemon = await response.json()
                print(pokemon['name'])


asyncio.run(send_pokemon())

print(time.time() - start)
