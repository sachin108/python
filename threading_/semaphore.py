import threading 
import time

cnt=threading.Semaphore(3)
# Create a semaphore that allows 3 concurrent accesses

def worker(id):
    print(f"worker {id} waiting")
    cnt.acquire()  # counter -= 1 (blocks if counter is 0)

    print(f"worker {id} is in!")
    time.sleep(2)

    print(f"worked {id} is leaving!")
    cnt.release()   # counter += 1

threads=[threading.Thread(target=worker, args=(i,)) for i in range (7)]

for t in threads:
    t.start()

for t in threads:
    t.join()

'''
worker 2 is in!
worker 1 is in!
worker 3 waiting
worker 6 waiting
worker 5 waiting
worked 0 is leaving!
worked 2 is leaving!
worker 4 is in!
worked 1 is leaving!
worker 3 is in!
worker 6 is in!
worked 3 is leaving!
worker 5 is in!
worked 4 is leaving!
worked 6 is leaving!
worked 5 is leaving!
'''


# Manually calling acquire() and release() is error-prone — if an exception happens between them, semaphore leak can happen. 
# Use with instead:

def worker(id):
    with cnt:              # acquire on enter, release on exit (even if exception)
        print(f"Worker {id} working")
        time.sleep(2)

# with guarantees release() runs no matter what

'''
A regular Semaphore lets us call release() more times than acquire(), which inflates the counter beyond its initial value. 
This is almost always a bug. It can be useful for dynamic capacity adjustment but might also lead to bugs.
'''
sem = threading.Semaphore(3)
sem.release()  # counter is now 4 — no error, but wrong!

bsem = threading.BoundedSemaphore(3)
bsem.release()  # raises ValueError — catches the bug