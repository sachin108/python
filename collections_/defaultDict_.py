from collections import defaultdict

# It is used to provide some default values for the key that does 
# not exist and never raises a KeyError.
d=defaultdict(int)
l=[1,2,3,1,2,4,1,5,6,8]

for i in l:
    # no need to check for the existence of i in d, if exists got it
    # else default will be 0
    d[i]+=1

    '''
      File "defaultDict_.py", line 11, in <module>
        d[i]+=1
      KeyError: 1    

      if d={}
    '''

print(d)