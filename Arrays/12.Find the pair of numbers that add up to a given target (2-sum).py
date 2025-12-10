#Find the pair of numbers that add up to a given target (2-sum).
from define import arr
ara = arr(10)
target = 9
def tsum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return arr[i],arr[j]
    return None
print(ara)
print(tsum(ara,9))