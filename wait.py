import asyncio
import aiohttp


async def show_status(session, url, delay):
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return f"status for {url} is {result.status}"


async def main():
    async with aiohttp.ClientSession() as session:
        requests = [
            asyncio.create_task(show_status(session, "https://www.wikipedia.org/", 5)),
            asyncio.create_task(show_status(session, "https://en.wikipedia.org/wiki/Persian_language", 3)),
            asyncio.create_task(show_status(session, "https://www.wissssskipedia.org/wiki/Persssephone", 9)),
            asyncio.create_task(show_status(session, "https://www.wikipedia.org/wiki/Persepolis", 7)),
        ]

        done, pending = await asyncio.wait(requests, return_when=asyncio.FIRST_EXCEPTION)

        print(done)
        print(pending)


asyncio.run(main())
