import asyncio


async def fire_event(condition):
    await asyncio.sleep(5)
    async with condition:
        print("notify all tasks...")
        condition.notify_all()
    print("notification finished")


async def do_work(condition, delay, n):
    print("start ", n)
    async with condition:
        print("locked ", n)
        await condition.wait()
        print("event happened... ", n)
        await asyncio.sleep(delay)
        print("work finished ", n)


async def main():
    condition = asyncio.Condition()
    fe = asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition, 10, 1), do_work(condition, 5, 2))
    await fe

asyncio.run(main())
