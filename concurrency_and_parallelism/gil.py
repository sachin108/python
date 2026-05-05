import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start) # 0.9896829128265381

import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start) # 0.9148321151733398
# two threads gave no speedup. If threading were truly parallel, we'd see ~0.5s. Instead we got ~0.91s — essentially 
# the same as single-threaded.
# point isn't "threaded is slower" — it's "threaded is not faster for CPU-bound work under the GIL."

'''
Use multithreading for I/O-bound work. When threads spend most of their time waiting — on network requests, database queries, 
            file reads, API calls — the GIL gets released during that wait. Other threads can run while one is blocked on I/O. 
            Threading is lighter weight here because threads share memory, so passing data between them is cheap. 

Use multiprocessing for CPU-bound work. When you need actual parallel computation — number crunching, image processing, 
            data transformation — each process gets its own interpreter and GIL, so you get true parallelism across cores. 
            The tradeoff is that processes are heavier: they have separate memory spaces, so sharing data between them 
            requires serialization (pickling), which adds overhead. Spawning a process is also slower than spawning a thread.
            Spawned process is a child process created by a parent process to execute a new program or command asynchronously, 
            allowing concurrent execution

Waiting on things → threading or asyncio
Computing things → multiprocessing or concurrent.futures.ProcessPoolExecutor

For many CPU-heavy tasks in Python, the best answer is actually neither. Libraries like NumPy, Pandas, and OpenCV do their 
heavy computation in C under the hood and release the GIL while doing so. So you get parallelism "for free" without needing to 
manage processes yourself. That's why in real-world Python, the GIL is less of a bottleneck than it sounds in theory — the 
performance-critical code is usually running outside of it.

Alternative Python interpreters: Python has multiple interpreter implementations. CPython, Jython, IronPython and PyPy, written 
in C, Java, C# and Python respectively, are the most popular ones. GIL exists only in the original Python implementation that 
is CPython. If your program, with its libraries, is available for one of the other implementations then you can try them out as well.
'''