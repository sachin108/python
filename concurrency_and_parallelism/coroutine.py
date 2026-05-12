import asyncio
async def greet():
    print("hello world")
    await asyncio.sleep(2)
    print("its a coroutine")

async def main():
    coroutine=greet()
    await coroutine

asyncio.run(main())

'''
In this example, greet() is a coroutine function that uses asyncio.sleep() to simulate a non-blocking task. The main() function 
calls greet() to create a coroutine object that you can await.
'''