import asyncio


async def trigger_event(event):
    await asyncio.sleep(5)
    event.set()


async def do_work_on_event(event, delay):
    print("waiting for event...")
    await asyncio.sleep(delay)
    await event.wait()
    print("performing work")
    await asyncio.sleep(delay)
    print("finished work")
    print(event.is_set())
    event.clear()
    print(event.is_set())


async def main():
    event = asyncio.Event()
    await asyncio.gather(do_work_on_event(event, 20), do_work_on_event(event, 2), trigger_event(event))


asyncio.run(main())
