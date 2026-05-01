'''
The with statement is used to wrap the execution of a block with methods defined by a context manager 
This allows common try…except…finally usage patterns to be encapsulated for convenient reuse.
'''

file=open("myfile.txt")
content=file.read()
file.close() # closing manually, but what if an exception occurs before closing?

# -------- using try - finally

file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
finally:
    file.close()

# -------------------------- using with statement

with open("hello.py") as file:  # open() function is a built-in context manager
    content=file.read()
    # f.close() is guaranteed to run, even on exceptions