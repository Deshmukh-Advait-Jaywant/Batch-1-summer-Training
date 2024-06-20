'''
ip:
    xyzabcdefklmnopqefgh

op:
    retunr the len of the longest substring
'''

s="abcdelmnoxyz"
m=0
cnt=1
for i in range(len(s)-1):
    if ord(s[i])==ord(s[i+1])-1:
        cnt+=1
    else:
        if m<cnt:
            m=cnt
        cnt=1
if m<cnt:
    m=cnt
print(m)
