'''

longest common subsequence

a="abcd"
b="axbdc"

op
    abd
'''

a="abcd"
b="axbd"
m=[]
for i in range(len(a)+1):
    l=[0]*(len(a)+1)
    m.append(l)
for i in range(1,len(a)+1):
    for j in range(1,len(b)+1):
        if a[i-1]==b[j-1]:
            m[i][j]=m[i-1][j-1]+1
        else:
            m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(a)][len(b)])

u=len(a)
v=len(b)
s=""
while u!=0 and v!=0:
    if a[u-1]==b[v-1]:
        s+=a[u-1]
        u-=1
        v-=1
    else:
        if m[u][v]==m[u][v-1]:
            v-=1
        elif m[u][v]==m[u-1][v]:
            u-=1
print(s[::-1])
                










