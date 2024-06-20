s1="10u5g2k1h1"
s2="g5g38d6h7"

s=set()
for i in s1:
    if i.isdigit():
        s.add(i)
for i in s2:
    if i.isdigit():
        s.add(i)
lis=list(s)
lis.sort()
for i in lis:
    if int(i)%2==0:
        es=i
        lis.remove(i)
        break
st=""
for i in range(len(lis)-1,-1,-1):
    st+=lis[i]
st+=es
print(st)
