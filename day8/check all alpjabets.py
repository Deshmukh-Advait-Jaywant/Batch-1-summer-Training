'''
ip:
    "the quick brown fox jumps over the lazy dog"
    


op:
    yes if all alphabets are there else no

'''

s="the 4quick br$%^own foENDx jum%&*ps o.ver the lazy dog"
d={}
for i in s:
    if i ==" ":
        continue
    if i not in d and i.islower():
        d[i]=1
print(d)
if len(d)==26:
    print("yes")
else:
    print("no")

