'''
Knowing the syntax is half the battle. The real skill is recognizing where to apply it. Any time you see setup/teardown 
pairs — acquire/release, connect/disconnect, start/stop, push/pop — a context manager is the right abstraction.
'''

# DB connection pools
from concurrent.futures import thread


with pool.acquire() as conn:
    conn.execute("Insert into ...")

# lock management - threading
with threading.lock():
    shared_state+=1

# exit stack for dynamic resources
from contextlib import ExitStack
with ExitStack() as stack:
    files=[stack.enter_context(open(f)) for f in filenames ]

# ... etc.
