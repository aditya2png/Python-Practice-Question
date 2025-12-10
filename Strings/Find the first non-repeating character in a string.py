##Find the first non-repeating character in a string.
stri = "abeieviahnbiaennz"
seen_once = []
seen_twice = []
for i in stri:
    if i in seen_twice:
        continue
    elif i in seen_once:
        seen_twice.append(i)
        seen_once.remove(i)
    else:
        seen_once.append(i)
print(seen_once[0])
    