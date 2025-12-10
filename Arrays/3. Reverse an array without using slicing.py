#Reverse an array without using slicing.


import numpy as np
def arr(n):
    nr = []
    
    for i in range(n):
        arr = np.random.randint(10)
        nr.append(arr)
    return nr

arra = arr(10)
print(arra)

rev = []

#pop method

while arra:
    a = arra.pop()
    rev.append(a)

#print(rev)

#method 2
for i in range(len(arra)-1,-1,-1):
    rev.append(arra[i])
print(rev)