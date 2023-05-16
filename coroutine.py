import asyncio
import datetime


async def one(name):
    await asyncio.sleep(2)
    print(f"Hello {name}")


# one("ahmad")
#
# print(type(one("ahmad")))
#
# print(one("ahmad"))

print(datetime.datetime.now())

asyncio.run(one("ahmad"))

asyncio.run(one("sajjad"))

print(datetime.datetime.now())


async def main():
    a = asyncio.create_task(one("ahmad"))
    b = asyncio.create_task(one("sajjad"))

    await a
    await b

print(datetime.datetime.now())

asyncio.run(main())

print(datetime.datetime.now())
