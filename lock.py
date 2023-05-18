import asyncio

counter = 0


# async def increment():
#     global counter
#     temp_counter = counter
#     temp_counter += 1
#     await asyncio.sleep(0.5)
#     counter = temp_counter


# async def increment():
#     global counter
#     temp_counter = counter
#     temp_counter += 1
#     # await asyncio.sleep(0.5)
#     counter = temp_counter

# async def increment(lock):
#     global counter
#     await lock.acquire()
#     temp_counter = counter
#     temp_counter += 1
#     await asyncio.sleep(0.5)
#     counter = temp_counter
#     lock.release()


async def increment(lock):
    global counter
    async with lock:
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(0.5)
        counter = temp_counter


async def main():
    global counter
    lock = asyncio.Lock()

    # task = [asyncio.create_task(increment(lock)) for _ in range(100)]

    # await asyncio.gather(*tasks)

    tasks = [increment(lock) for _ in range(10)]

    for task in asyncio.as_completed(tasks):
        await task

    print(counter)

asyncio.run(main())
