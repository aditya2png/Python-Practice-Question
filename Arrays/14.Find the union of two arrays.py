#Find the union of two arrays.
from define import arr
arr1 = arr(5)
arr2 = arr(5)
def union(a,b):
    u = []
    for i in a:
        if i not in u:
            u.append(i)
    for i in b:
        if i not in u:
            u.append(i)
    return u

print(arr1,arr2,union(arr1,arr2))