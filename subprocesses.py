import asyncio
from asyncio.subprocess import PIPE


# async def main():
#     process = await asyncio.create_subprocess_exec("ls", "-l")
#     print("process id is :", process.pid)
#     status_code = await process.wait()
#     print("status code is :", status_code)





# async def main():
#     process = await asyncio.create_subprocess_exec("sleep", "5")
#     print(process.pid)
#     try:
#         status_code = await asyncio.wait_for(process.wait(), 2)
#         print(status_code)
#     except asyncio.TimeoutError:
#         print("time out process")
#         # process.terminate()
#         process.kill()
#         status_code = await process.wait()
#         print(status_code)


async def main():
    process = await asyncio.create_subprocess_exec("python", "test.py", stdin=PIPE, stdout=PIPE)
    std_out, std_err = await process.communicate(b'ahmad')
    print(std_out)
    print(std_err)


asyncio.run(main())
