'''
ip:
    "placements"

op:
    replace all consonants in lowercase
    and vowels in uppercase

    plAcEmEnts
'''

s="placEments"
s1="School"
res=""
for i in s:
    if i in "aeiouAEIOU":
        res=res+i.upper()
    else:
        res=res+i.lower()
print(res)
