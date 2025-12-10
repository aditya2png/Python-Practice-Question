#Remove all duplicate characters from a string.
stri = "aniaiubfeiWniw"
new = ""
for i in stri.lower():
    if i not in new:
        new+=i
print(new)