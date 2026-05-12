The Python Global Interpreter Lock or GIL is a mutex (or a lock) that allows only one thread to hold the control of the 
Python interpreter.
    
    MUTEX - Mutual Exclusion: Only one thread can hold the lock, ensuring data integrity.

This means that only one thread can be in a state of execution at any point in time. The impact of the GIL isn’t visible 
to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded 
code.

What Problem Did the GIL Solve for Python?
    Python uses reference counting for memory management. It means that objects created in Python have a reference count 
    variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory 
    occupied by the object is released.

    >>> import sys
    >>> a = []
    >>> b = a
    >>> sys.getrefcount(a)
    3

    In the above example, the reference count for the empty list object [] was 3. The list object was referenced by a, b and 
    the argument passed to sys.getrefcount().

The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease 
its value simultaneously. If this happens, it can cause either leaked memory that is never released or, even worse, incorrectly 
release the memory while a reference to that object still exists. This can cause crashes or other “weird” bugs in Python programs.

This reference count variable can be kept safe by adding locks to all data structures that are shared across threads so that 
they are not modified inconsistently.

But adding a lock to each object or groups of objects means multiple locks will exist which can cause another problem—Deadlocks
(deadlocks can only happen if there is more than one lock). Another side effect would be decreased performance caused by the 
repeated acquisition and release of locks.

The GIL is a single lock on the interpreter itself which adds a rule that execution of any Python bytecode requires acquiring 
the interpreter lock. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. 
But it effectively makes any CPU-bound Python program single-threaded.

This mutex is necessary mainly because CPython's memory management is not thread-safe.

Jython and IronPython have no GIL and can fully exploit multiprocessor systems
PyPy currently has a GIL like CPython
In Cython the GIL exists, but can be released temporarily using a "with" statement
