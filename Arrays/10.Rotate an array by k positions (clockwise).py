#Rotate an array by k positions (clockwise).
from define import arr
new = arr(10)

k = 3
print(new)
x = len(new)
rot = [0]*x
for i in range(x):
    ni = (i-k)%x 
    rot[ni]=new[i]
print(rot)