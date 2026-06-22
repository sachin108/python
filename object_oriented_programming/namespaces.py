var1="Hello"
def greet():
    name="Jon"
    return var1+"   "+name

'''
Python stores the names of variables, functions and classes in NAMESPACES. This helps organize names and prevents conflicts when 
the same name is used in different parts of a program. Internally, namespaces are implemented using dictionaries.
'''

# TYPES OF NAMESPACES
'''
1. Built - in -- print, len, str, list, dict, int, Exception .. These are objects stored in the built-in namespace.

2. Global - contains names that are created at the top level of a program, outside all functions and classes. These can usually 
            be accessed from anywhere within the same module. eg: var1

3. Local - created whenever a function is called. Variables defined inside the function are stored in this namespace. These 
            variables are available only while the function is executing. eg: name

The built-in namespace exists as long as the Python interpreter is running.

The global namespace exists until the program finishes execution.

A local namespace exists only while its function is running.
'''
