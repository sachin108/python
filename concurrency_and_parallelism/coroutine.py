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

Using the async def construct, we can define a coroutine function. It may use await, return, or yield, but all of these 
are optional:
    await, return, or both can be used in regular coroutine functions. To call a coroutine function, must either await it 
    to get its result or run it directly in an event loop.
    
    yield used in an async def function creates an asynchronous generator. To iterate over this generator, we can use an 
    async for loop or a comprehension.
    
    async def may not use yield from, which will raise a SyntaxError.
'''

async def z(x):
    pass

async def gen(x):
    pass

async def f(x):
    y = await z(x)  # Okay - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # Okay - this is an async generator

# wrong
# async def m(x):
#     yield from gen(x) 

# OK
def m(x):
    yield from gen(x) 
# yield from is valid only in a regular def (not async def)

async def n(x):
    y = await z(x)  
    return y