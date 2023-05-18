import asyncio
import aiohttp


async def show_status(session, url, delay):
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        print(f"status for {url} is {result.status}")


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            show_status(session, "https://www.wikipedia.org/", 5),
            show_status(session, "https://en.wikipedia.org/wiki/Persian_language", 3),
            show_status(session, "https://www.wikipedia.org/wiki/Persephone", 9),
            show_status(session, "https://www.wikipedia.org/wiki/Persepolis", 7),
        ]

        for request in asyncio.as_completed(requests):
            await request

asyncio.run(main())
