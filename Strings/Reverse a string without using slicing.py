#Reverse a string without using slicing.

stri = 'aditya'
rev = ''
for i in range(len(stri)-1,-1,-1):
    rev+=stri[i]
print(rev)