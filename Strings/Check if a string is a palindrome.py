#Check if a string is a palindrome.
stri = "eve"
check = ""
for i in range(len(stri)-1,-1,-1):
    check+=stri[i]
if check==stri:
    print("string is palindrom")
else:
    print("no palindrome")