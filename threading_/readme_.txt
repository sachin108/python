Each program is a process and has at least one thread that executes instructions for that process.

The threading module provides a way to run multiple threads (smaller units of a process) concurrently within a single process. 
It allows for the creation and management of threads, making it possible to execute tasks in parallel, sharing memory space. 
Threads are particularly useful when tasks are I/O bound, such as file operations or making network requests, where much of 
the time is spent waiting for external resources.

Unlike the multiprocessing module, which uses separate processes to bypass the global interpreter lock (GIL), the threading 
module operates within a single process, meaning that all threads share the same memory space.

The code in new threads may or may not be executed in parallel (at the same time), even though the threads are executed 
concurrently. There are a number of reasons for this, such as:
    *   The underlying hardware may or may not support parallel execution (e.g. one vs multiple CPU cores).
    *   The Python interpreter may or may not permit multiple threads to execute in parallel.

A Python thread may progress through three steps of its life-cycle: a new thread, a running thread, and a terminated thread
While running, the thread may be executing code or may be blocked, waiting on something such as another thread or an external 
resource. Although, not all threads may block, it is optional based on the specific use case for the new thread.
    New Thread
    Running Thread
        Blocked Thread (optional)
    Terminated Thread

A new thread is a thread that has been constructed by creating an instance of the threading.Thread class.
A new thread can transition to a running thread by calling the start() function.

A running thread may block in many ways, such as reading or writing from a file or a socket or by waiting on a concurrency 
primitive such as a semaphore or a lock. After blocking, the thread will run again.

Finally, a thread may terminate once it has finished executing its code or by raising an error or exception.