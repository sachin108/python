from collections import OrderedDict

# Dictionary that remembers insertion order, making it useful for order-sensitive operations.

od=OrderedDict()
od['a']=1
od['c']=3
od['b']=2
od['d']=4
print(od) # OrderedDict([('a', 1), ('c', 3), ('b', 2), ('d', 4)])

for k, v in od.items():
    print(f"key={k}, value={v}")
    '''
        key=a, value=1
        key=c, value=3
        key=b, value=2
        key=d, value=4
    '''