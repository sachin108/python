'''
Generators are functions that produce a sequence of values lazily — one at a time, on demand — instead of computing 
everything upfront and storing it in memory. 

A generator is a function that returns a generator iterator. The returned object allows you to iterate over data 
without the need to store the entire dataset in memory at once. Instead, generator iterators yield items one at 
a time and only when requested, making them memory efficient.

We can create a generator using the yield keyword inside a function.

Generators are particularly useful when working with large datasets or streams of data where you don’t want to 
load everything into memory at once. They provide a lazy data generation mechanism, meaning values are computed on 
demand. This can significantly improve performance and reduce memory usage in your programs.

A regular function computes a result, returns it, and forgets everything. A generator pauses execution at each 
yield, remembers its entire local state, and resumes exactly where it left off when the next value is requested. T
his makes them ideal when you need to:
    Process datasets too large to fit in memory
    Build pipelines that transform data step by step
    Represent infinite or very long sequences
    Write cleaner code where a loop-with-accumulator pattern would otherwise appear

Any function containing yield becomes a generator function.     
'''

def countdown(n):
    while n>0:
        yield n
        n-=1

x=countdown(3)  # No code runs yet
print(next(x))  # 3  — runs until first yield
print(next(x))  # 2  — resumes, runs until next yield
print(next(x))  # 1
print(next(x))

'''
3
2
1
Traceback (most recent call last):
  File "generator.py", line 35, in <module>
    print(next(x))
StopIteration
'''

def my_generator():
  yield 1
  yield 2
  yield 3

for i in my_generator():
  print(i)

'''
1
2
3

generators in general yield as many times as they like, but @contextmanager imposes a one-yield contract because 
it's repurposing the yield as the boundary between setup and teardown.
'''

def func():
    print("hello")
    yield 1
    print("Now")
    
y=func()
print(f"y={y}")
print(next(y))
print(next(y))
'''
y=<generator object func at 0x7efdfcc3a380>
hello
1
Now
Traceback (most recent call last):
  File "<main.py>", line 9, in <module>
StopIteration


When Python sees yield, it compiles the function as a generator. Each call to next() executes code up to the next 
yield, suspends the frame (local variables, instruction pointer), and returns the yielded value. The frame stays 
alive on the heap until the generator is exhausted or garbage-collected.

You rarely call next() manually. Generators plug directly into for loops, comprehensions, and any function expecting 
an iterable:
'''
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)

'''
5
4
3
2
1

The for loop calls next() internally and catches StopIteration for you.
'''

# Generator Expressions
squares = (x ** 2 for x in range (1000))
# This creates no list in memory. Values are computed one at a time as they're consumed. This is effective 
# because the memory footprint stays constant regardless of the range size — only one squared value exists at a time.

# Sum of squares without ever building a million-element list
total = sum(x ** 2 for x in range(1_000_000))


# Generators support .close() and .throw() for lifecycle management:
def managed_resource():
    print("Acquiring resource")
    try:
        while True:
            data = yield
            print(f"Processing: {data}")
    except GeneratorExit:
        print("Cleaning up resource")

gen = managed_resource()
next(gen)
gen.send("item 1")
gen.close()          # Raises GeneratorExit inside the generator
'''
Output:
Acquiring resource
Processing: item 1
Cleaning up resource
'''

# Generators are single-use. Once exhausted, they produce nothing:
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] — already exhausted


# Generators are lazy, including errors. A bug inside a generator won't surface until that value is requested.
def bad_gen():
    yield 1
    raise ValueError("oops")
    yield 3

gen = bad_gen()       # No error here
print(next(gen))      # 1 — still fine
print(next(gen))      # ValueError raised HERE, not at definition


'''
@contextmanager generators are a special, constrained use case. The decorator expects the generator to yield exactly 
once because it maps the generator's structure onto the with statement
Code before yield is the setup (__enter__), code after is the teardown (__exit__). 

If you yielded twice inside a @contextmanager, the decorator wouldn't know what to do with the second value — it 
would raise a RuntimeError.
'''
from contextlib import contextmanager

@contextmanager
def temp_directory():
    import tempfile, shutil
    path = tempfile.mkdtemp()
    try:
        yield path      #  this is what 'as' receives
    finally:
        shutil.rmtree(path)  # cleanup always runs

with temp_directory() as tmpdir:
    print(f"Working in {tmpdir}")