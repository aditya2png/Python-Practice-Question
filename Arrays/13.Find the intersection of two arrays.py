#Find the intersection of two arrays.
from define import arr
arr1 = arr(10)
arr2 = arr(10)

def intersect(arr1,arr2):
    intersect = []
    for i in arr1:
        if i in arr2 and i not in intersect:
            intersect.append(i)
        
    return intersect
print(arr1,arr2)
print(intersect(arr1,arr2))