#Count the frequency of each element in a list.
from define import arr
def count(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

ara = arr(10)
print(ara)
print(count(ara))