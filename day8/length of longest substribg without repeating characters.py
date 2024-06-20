'''
ip:
    "djsfisehfyusgrvujsbdk"
op:

    print the length of longest substring with non repeating characters
'''
s="abfgresagtyuiofde"
l=""
d={}
m=0
i=0
while i<len(s):
    while i<len(s):
        if s[i] not in l:
            l+=s[i]
            d[l[i]]=i
        else:
            m=max(m,len(l))
            l=""
            break
        i+=1
        print(d)
    i=d[s[i]]+1
print(m)

