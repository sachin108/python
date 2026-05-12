import asyncio

async def greet():
    print("one")
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(greet(), greet(), greet())

if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

'''
one
one
one
two
two
two
with_coroutine.py executed in 2.00 seconds.

Now, we are using the async keyword to turn count() into a coroutine function that prints One, waits for one second, then prints Two, 
and waits another second. We use the await keyword to await the execution of asyncio.sleep(). This gives the control back to the 
program’s event loop, saying: I will sleep for one second. Go ahead and run something else in the meantime.

The main() function is another coroutine function that uses asyncio.gather() to run three instances of count() concurrently. 
'''