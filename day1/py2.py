'''
ip:
    f46flj85saoib3^32*5@^%JKSAE
op:
    lowercaseVowels:3
    uppercaseVowels:2
    lowercaseConsonats:
    uppercaseconsonants
    digits
    special chars
'''
s="f46flj85saoib3^32*5@^%JKSAE"

lowercaseVowels=0
uppercaseVowels=0
lowercaseConsonats=0
uppercaseconsonants=0
digit=0
special_chars=0

for i in s:
    if i.isnumeric():
        digit+=1
    elif i.isupper():
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            uppercaseVowels+=1
        else:
            uppercaseconsonants+=1
    elif i.islower():
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            lowercaseVowels+=1
        else:
            lowercaseConsonats+=1
    elif not i.isalnum():
        special_chars+=1


print("digits",digit)
print("uppercaseVowels",uppercaseVowels)
print("uppercaseconsonants",uppercaseconsonants)
print("lowercaseVowels",lowercaseVowels)
print("lowercaseConsonats",lowercaseConsonats)
print("special_chars",special_chars)




            
