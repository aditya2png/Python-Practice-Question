#Find the missing number in an array of 1 to n.
n = 5  
Array = [1, 2, 4, 5]
new_arr = [x for x in range(1,6)]
print(new_arr)
for i in new_arr:
    if i not in Array:
        print("missing number: ",i)