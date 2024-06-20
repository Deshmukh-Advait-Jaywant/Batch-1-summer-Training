'''
using recrussion print the sum of
ip:
    a=[3,8,5,4,3]
    b=[5,0,9,3,2]
op:
    (even sum , odd sum) =>(12,17)

def se(idx,a,b,sume,sumo):
    if idx==len(a):
        return (sume,sumo)
    if a[idx]%2==0:
        sume+=a[idx]
    if b[idx]%2!=0:
        sumo+=b[idx]
    return se(idx+1,a,b,sume,sumo)


       


a=[3,8,5,4,3]
b=[5,0,9,3,2]

print(se(0,a,b,0,0))
'''
'''
def s(i,n,se):
    if i>=n+1:
        return se
    se=se+i
    return s(i+2,n,se)
    
n=10
print(s(0,n,0))
'''
l=[1,23,4,5,6,7,8]
'''
if len(l)%2==0:
    print("yes")
else:
    print("no")
    '''
'''
c=0
j=-1
i=0
while i<=j:
    if l[i]==l[j] and i<=j:
        print(i)
        
        
    i+=1
    j-=1
print(i)        '''



print(l.remove())

print(l)







