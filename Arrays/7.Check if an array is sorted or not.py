#Check if an array is sorted or not.

from define import arr
checker = [1,2,3,4,5,6]

def sorty(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return "not sorted"
        else:
            return "sorted"

print(sorty(checker))

