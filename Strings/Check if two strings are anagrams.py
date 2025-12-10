#Check if two strings are anagrams.

#method 1
stri = "aditya"
stri2 = "aytida"

if sorted(stri) == sorted(stri2):
    print("they are anagrams")
else:
    print("nope")

