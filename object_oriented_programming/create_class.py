class Vehicle:
    type="Four Wheelers"  # class attribute, meaning it is shared by all instances of the class
    
    # __init__ is a constructor method that runs automatically when a new object is created. Itmis used to initialize object data.
    # It defines the properties that all class objects must have.
    # Every time we create a new object, .__init__() sets the initial state of the object by assigning the values of the object’s properties.
    def __init__(self, name):
        self.name=name

    # self refers to the current object, allowing each object to store and access its own data

v1=Vehicle("Car")
v2=Vehicle("Truck")

print(f"name of v1 = {v1.name} and it is of type {Vehicle.type}")
print(f"name of v2 = {v2.name} and it is of type {Vehicle.type}")

'''
And why do you even need classes in the first place? 

Primitive data structures—like numbers, strings, and lists—are designed to represent straightforward pieces of information, 
such as the cost of an apple, the name of a poem, or your favorite colors, respectively. 
What if you want to represent something more complex?

For example, you might want to track employees in an organization. You need to store some basic information about each employee, 
such as their name, age, position, and the year they started working.

One way to do so -- represent each employee as a list:
    kirk = ["James Kirk", 34, "Captain", 2265]
    spock = ["Spock", 35, "Science Officer", 2254]
    mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

Issues with this approach:
    it can make larger code files more difficult to manage. If you reference kirk[0] several lines away from where you declared 
    the kirk list, will you remember that the element with index 0 is the employee’s name?

    it can introduce errors if employees don’t have the same number of elements in their respective lists. In the mccoy list above, 
    the age is missing, so mccoy[1] will return "Chief Medical Officer" instead of Dr. McCoy’s age.    

A great way to make this type of code more manageable and more maintainable is to use classes.

Classes allow to create user-defined data structures. Classes define functions called methods, which identify the behaviors and 
actions that an object created from the class can perform with its data.

While the class is the blueprint, an instance is an object that’s built from a class and contains real data. An instance of the Dog 
class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.

A class is like a form. An instance is like a form that you’ve filled out with information

Attributes created in .__init__() are called instance attributes.
Class attributes are attributes that have the same value for all class instances.
'''

class Dog:
    species = "Canis familiaris"   # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age

    # Instance method - functions that can only call on an instance of that class. 
    # Just like .__init__(), an instance method always takes self as its first parameter.
    def description(self):
        return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
cero=Dog("cero", 14)

print(cero) # <__main__.Dog object at 0x00aeff70>
# add __str__ in class to get a string containing information about the Dog instance

# after adding __str__()
print(cero) # 'cero is 14 years old'


