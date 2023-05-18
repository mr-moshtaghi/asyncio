import asyncio


# async def show(smp):
#     await smp.acquire()
#     print("show methode....")
#     await asyncio.sleep(0.5)
#     smp.release()


async def show(smp):
    async with smp:
        print("show methode....")
        await asyncio.sleep(0.5)


async def main():
    smp = asyncio.Semaphore(2)
    # smp = asyncio.BoundedSemaphore(2)
    tasks = [asyncio.create_task(show(smp)) for _ in range(10)]

    await asyncio.gather(*tasks)

asyncio.run(main())
