#1. Write a program to find the maximum and minimum element in an array.
import numpy as np
nr = []
for i in range(10):
    arr = np.random.randint(10)
    nr.append(arr)

maxi = float("-inf")
mini = float("inf")
for num in nr:
    if num>maxi:
        maxi = num
    if num<mini:
        mini = num
print("array is: ",nr)
# print("Maximum number is : ",maxi)
# print("Minimum number is : ",mini)




