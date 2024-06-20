'''
s="leet**cod*e"
res=[]
s1=""
for i in s:
    if i != '*':
        res.append(i)
    elif i=="*":
        res.pop()
for i in res:
    s1+=i
print(s1)
'''

st="is2 sentence4 This1 a3"
s=""
for i in range(len(st)):
    if st[i] in [1,2,3,4,5,6,7,8,9]:
        s=" "
    else:
        s+=st[i]
