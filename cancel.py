import asyncio
from asyncio import CancelledError, TimeoutError


async def one():
    print("Hello")
    await asyncio.sleep(10)
    print("world")


# async def main():
#     a = asyncio.create_task(one())
#
#     sec = 0
#     while not a.done():
#         print("task is not finished")
#         await asyncio.sleep(1)
#         sec += 1
#         if sec == 5:
#             a.cancel()
#
#     try:
#         await a
#     except CancelledError:
#         print("task cancelled")






# async def main():
#     a = asyncio.create_task(one())
#
#     try:
#         await asyncio.wait_for(a, timeout=5)
#     except TimeoutError:
#         print("task cancelled")
#
#     print(f'was task cancelled : {a.cancelled()}')




async def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(asyncio.shield(a), timeout=5)
    except TimeoutError:
        print("Task is taking longer than time usual, but we are working on it")
        print(f'was task cancelled : {a.cancelled()}')
        await a


asyncio.run(main())
