# double ended queue

from collections import deque

dq=deque([2,3,4])
print(f"dq before inserting elements {dq}")

dq.append(5) # appended at last of the queue
dq.appendleft(1) # appended at the starting of the queue

print(f"dq after inserting elements {dq}")

dq.pop()
print(f"dq after removing last element {dq}")

dq.popleft()
print(f"dq after removing first element {dq}")

'''
dq before inserting elements deque([2, 3, 4])
dq after inserting elements deque([1, 2, 3, 4, 5])
dq after removing last element deque([1, 2, 3, 4])
dq after removing first element deque([2, 3, 4])
'''