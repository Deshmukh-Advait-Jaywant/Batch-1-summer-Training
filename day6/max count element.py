'''
[4,8,2,4,4,8,4]

print element which has count more than half length


'''
l=[1,1,2,1,1,3]
'''
m=max(l)
cnt=[0 for i in range(m+1)]
le=len(l)
for i in range(le):
    cnt[l[i]-1]+=1
print(cnt)

for i in range(len(cnt)):
    if cnt[i]>le//2:
        print(i+1)
'''
'''
l.sort()
print(l[(0+(len(l)//2))//2])
'''
c=1
x=l[0]
for i in range(1,len(l)):
    if x==l[i]:
        c+=1
    elif c>0:
        c-=1
    elif c==0:
        c+=1
        x=l[i]
print(x)
