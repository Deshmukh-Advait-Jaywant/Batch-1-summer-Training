def fun(i,j,m,cnt,vi,a,b):
    if i==a and j==b:
        return cnt
    if (i,j) in vi:
        return cnt
    else:
        vi.append((i,j))
    if i==r-1 and j==c-1:
        cnt+=1
        print(vi)
        vi.pop()
        return cnt
    if i<r-1:
        cnt=fun(i+1,j,m,cnt,vi,a,b)
    if i> 0:
        cnt=fun(i-1,j,m,cnt,vi,a,b)
    if j<c-1:
        cnt=fun(i,j+1,m,cnt,vi,a,b)
    if j>0:
        cnt=fun(i,j-1,m,cnt,vi,a,b)
    vi.pop()
    return cnt
r=int(input())
c=int(input())

#obstructle cordinates
a=int(input())
b=int(input())
m=[]
for i in range(r):
    l=[]
    for j in range(c):
        l.append("-")
    m.append(l)
print(m)
print(fun(0,0,m,0,[],a,b))
