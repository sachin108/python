# we can define custom context managers as well
class MyContextManager:
    def __init__(self):
        print("INSIDE __init__")

    # __enter__(): Acquires the resource and returns it
    # called by the with statement to enter the runtime context.
    def __enter__(self):
        print("INSIDE __enter__")

    # __exit__(): cleans up the resource (e.g., closes a file).
        # the __exit__ method is only called if the __enter__ method and with code block completes successfully    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("INSIDE __exit__")
        if exc_type:
            print(f"Caught an error: {exc_value}")
            # Returning True "swallows" the error so the script doesn't crash
            return True
        
with MyContextManager() as mine:
    print("Let's Go!")
    raise TypeError("just chill!!")

    '''
    Without TypeError
        INSIDE __init__
        INSIDE __enter__
        Let's Go!
        INSIDE __exit__ 

    With TypeError    
        INSIDE __init__
        INSIDE __enter__
        Let's Go!
        INSIDE __exit__
        Caught an error: just chill!!    
    '''


# Measuring Execution Time
from time import perf_counter, sleep

class Timer:
    def __enter__(self):
        self.start = perf_counter()

    def __exit__(self, *_):
        end = perf_counter()
        print(f"Elapsed time: {end - self.start:.4f} seconds")


with Timer():
     # The code for which the time is to be calculated
     sleep(0.5)