from Timer import *

# we can define custom context managers as well
class MyContextManager:
    def __init__(self):
        print("INSIDE __init__")

    # __enter__(): Acquires the resource and returns it
    # called by the with statement to enter the runtime context.
    # Its return value is bound to the with target variable.
    def __enter__(self):
        print("INSIDE __enter__")

    # This method handles the teardown logic and is automatically called when the flow of execution leaves the 
    # with block. If an exception occurs, then exc_type, exc_value, and exc_tb hold the exception type, value, 
    # and traceback information, respectively.  
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("INSIDE __exit__")
        if exc_type:
            print(f"Caught an error: {exc_value}")
            # Returning True "swallows" the error so the script doesn't crash
            return True
    '''
        If the .__exit__() method returns True, then any exception that occurs in the with block is swallowed and 
        the execution continues at the next statement after with. If .__exit__() returns False, then exceptions are 
        propagated out of the context. This is also the default behavior when the method doesn’t return anything explicitly.     
    '''
    
# To create an asynchronous context manager, need to define the .__aenter__() and .__aexit__() methods. 
with Timer():        
    sleep(1)
    with MyContextManager() as mine:
        print("Let's Go!")
        x=1/0
print("even after error occurred") # if exit returns true

'''
Without x=1/0
    INSIDE __init__
    INSIDE __enter__
    Let's Go!
    INSIDE __exit__ 

With x=1/0     -- if __exit__() returns True
    INSIDE __init__
    INSIDE __enter__
    Let's Go!
    INSIDE __exit__
    Caught an error: division by zero
    Elapsed time: 1.0052 seconds
    even after error occurred

With x=1/0     -- if __exit__() returns False
    INSIDE __init__
    INSIDE __enter__
    Let's Go!
    INSIDE __exit__
    Caught an error: division by zero
    Elapsed time: 1.0037 seconds
    Traceback (most recent call last):
    File "Custom_Context_Manager.py", line 34, in <module>
        x=1/0
    ZeroDivisionError: division by zero
'''
