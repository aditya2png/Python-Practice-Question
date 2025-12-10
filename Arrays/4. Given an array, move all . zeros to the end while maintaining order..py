#Given an array, move all zeros to the end while maintaining order.
from define import arr
new_array = arr(10)
print(new_array)
zero = []
non_zero = []
for i in new_array:
    if i == 0:
        zero.append(i)
    else:
        non_zero.append(i)

non_zero.extend(zero)
print(non_zero)
