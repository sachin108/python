from collections import namedtuple

student=namedtuple('Student', ['name', 'age', 'DOB'])

s1=student('Suahni', '19', '08/08/2006')

print(f"name of the student is {s1.name}") # Access using index 

print(f"age of the student is {s1[1]}") # Access using name  

'''
like a regular tuple but with named fields, making data more readable and accessible. Instead of 
using indexes, we can access elements by name, improves code clarity and ease of use.
'''