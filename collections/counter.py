from collections import Counter
'''
Counter is a subclass of Python’s dict from the collections module. It is mainly used to count the 
frequency of elements in an iterable (like lists, strings or tuples) or from a mapping (dictionary).

class Counter(dict):
    ....
    ....
'''

nums=[1,2,3,1,1,2,4,3]
x=Counter(nums)
print(x) #   Counter({1: 3, 2: 2, 3: 2, 4: 1})

y="mycarmy"
cnt=Counter(y)
print(cnt) #   Counter({'m': 2, 'y': 2, 'c': 1, 'a': 1, 'r': 1})
print(cnt['m']) # 2

# for dicts it will remain same
z={1: 2, 2: 3, 3: 1}
print(Counter(z)) # Counter({2: 3, 1: 2, 3: 1})

print(f"most common element in counter x={x.most_common(1)}") # x=[(1, 3)]
print(f"2 most common elements in counter x={x.most_common(2)}") #  x=[(1, 3), (2, 2)]