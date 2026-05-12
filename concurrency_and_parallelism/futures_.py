'''
A future represents a computation that hasn't completed yet. It's a placeholder object that will eventually hold a result 
(or an exception). The reason this abstraction is so useful is that it decouples submitting work from waiting for the result — you 
can kick off multiple tasks and collect results later, which is the foundation of concurrent programming.

Python provides futures through the concurrent.futures module, which offers two executors: ThreadPoolExecutor (for I/O-bound work) 
and ProcessPoolExecutor (for CPU-bound work).
'''

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time
from unittest import result

def fetch_data(url):
    time.sleep(1)
    return f"data from {url}"

urls=['site-a.com', 'site-b.com', 'site-c.com']

with ThreadPoolExecutor(max_workers=3) as executor:
    futures={executor.submit(fetch_data, url): url for url in urls}

    # as_completed() yields futures in the order they finish, not the order 
    # they were submitted — so we can process results as soon as they're available.
    for future in as_completed(futures):
        url=futures[future]
        
        result=future.result()
        # Futures capture exceptions rather than raising them at submission time. The exception surfaces when we call .result():
        
        print(f"{url} -> {result}")

# Callbacks: reacting when a future completes

def on_done(future):
    print(f"Completed with: {future.result()}")

with ThreadPoolExecutor() as executor:
    f = executor.submit(fetch_data, "site-a.com")
    f.add_done_callback(on_done)


# we also haev ProcessPoolExecutor for CPU-bound work

# Python's asyncio module has its own Future type for single-threaded async code. It's conceptually the same — a placeholder for a 
# pending result — but it works within an event loop rather than with OS threads. 
# The mental model is the same: submit work, get a handle, collect results later. 

