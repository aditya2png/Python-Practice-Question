#Find the longest word in a sentence.
stri = "My name is Aditya and i like to play valorant"
lis = stri.split()
longest = "" 
current = ""
for i in lis:
    if len(i)>len(longest):
        longest = i
print(longest)
