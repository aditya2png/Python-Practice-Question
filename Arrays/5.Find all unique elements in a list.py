#Find all unique elements in a list.

from define import arr
uniq = []
normal = arr(10)

for i in normal:
    if i in uniq:
        pass
    else:
        uniq.append(i)
print(normal)
print(uniq)