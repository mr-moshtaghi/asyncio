

import asyncio

# loop = asyncio.get_event_loop()
# f = loop.create_future()

# f = asyncio.Future()
#
# print(f.done())
# print(f.done())
# print(f.result())


async def set_after(future, delay, value):
    await asyncio.sleep(delay)
    future.set_result(value)


async def main():
    # future = asyncio.Future()

    loop = asyncio.get_running_loop()
    future = loop.create_future()

    loop.create_task(
        set_after(future, 3, 'ahmad')
    )
    print("hello ")

    print(future.done())

    # result = await future

    print(future.done())

    # print(result)

    print(future.result())

asyncio.run(main())




