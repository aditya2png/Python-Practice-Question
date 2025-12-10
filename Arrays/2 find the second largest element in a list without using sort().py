#2 find the second largest element in a list without using sort().

max = float("-inf")
second_max = float("-inf")

ar = [2,5,1,6,6,35,6332,232]
for num in ar:
    if num>max:
        second_max=max
        max=num
    elif max>num>second_max:
        second_max=num

print(second_max)
print(max)