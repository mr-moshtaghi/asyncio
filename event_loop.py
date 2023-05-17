import asyncio
import datetime


async def one(name):
    await asyncio.sleep(2)
    print(f"Hello {name}")


async def main():
    a = asyncio.create_task(one("ahmad"))
    b = asyncio.create_task(one("sajjad"))

    await a
    await b

loop = asyncio.new_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()

