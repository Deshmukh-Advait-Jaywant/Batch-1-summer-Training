def fun(i,j,m,cnt,a,b):
    if i==a and j==b:
        return cnt
    if i==r-1 and j==c-1:
        cnt+=1
        return cnt
    if i<r-1:
        cnt=fun(i+1,j,m,cnt,a,b)
    if j<c-1:
        cnt=fun(i,j+1,m,cnt,a,b)

    return cnt



r=int(input())
c=int(input())
a=int(input())
b=int(input())
m=[]

for i in range(r):
    l=[]
    for j in range(c):
        l.append("-")
    m.append(l)
print(m)
print(fun(0,0,m,0,a,b))
