#Count vowels and consonants in a string.
vowels = ['a', 'e', 'i', 'o', 'u']
stri = "hello mister how do you do"
vowel_count = 0
consonant_count = 0
for i in stri:
    if i in vowels:
        vowel_count+=1
    else:
        consonant_count+=1
print(vowel_count,consonant_count)