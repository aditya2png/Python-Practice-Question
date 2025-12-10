#Count the frequency of each character.
stri = 'asbhebitb'
freq = {}
for i in stri:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
print(freq)