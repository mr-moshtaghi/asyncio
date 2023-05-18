import asyncio
import aiohttp


async def show_status(session, url):
    async with session.get(url) as result:
        return result.status


# async def main():
#     async with aiohttp.ClientSession() as session:
#         url = "https://www.wikipedia.org/"
#         status = await show_status(session, url)
#         print(f'status is {status}')



async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://www.wikipedia.org/", "https://en.wikipedssssssia.org/wiki/Persian",
                "https://en.wikipedia.org/wiki/Persian_language", "https://en.wikipedia.org/wiki/Persian_Gulf",
                "https://en.wikipedia.org/wiki/Persian_Jews"]

        requests = [show_status(session, url) for url in urls]
        statuses = await asyncio.gather(*requests, return_exceptions=True)
        print(statuses)


asyncio.run(main())
