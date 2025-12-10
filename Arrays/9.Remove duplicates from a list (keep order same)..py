from define import arr

#Remove duplicates from a list (keep order same).

lis = arr(10)
print(lis)
new_lis = []
for i in lis:
    if i in new_lis:
        pass
    else:
        new_lis.append(i)
print(new_lis)