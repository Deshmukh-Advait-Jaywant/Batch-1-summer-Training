'''
n=12
k=2
for i in range(n,-1,-1):
    if n%i==0:
        k-=1
        if k==0:
            print(i)
            break
'''
'''
def fact(n,k,i):
    if k==0:
        return i+1
    if n%i==0:
        k-=1
    return fact(n,k,i-1)
n=12
k=3
print(fact(n,k,n))
'''

'''
#coprime or not
n=int(input())
m=int(input())
nL=set()
mL=set()
for i in range(2,n):
    if n%i==0:
        nL.add(i)
for j in range(2,m):
    if m%j ==0:
        mL.add(j)

if nL.intersection(mL):
    print("no cop")
else:
    print("cp")

import math
print(math.gcd(4,5def))
if math.gcd(4,7) ==1:
    print("cp")
else:
    print("ncp")
'''
a=int(input())
b=int(input())
for i in range(2,(min(a,b)//2)+1):
    if a%i==0 and b%i==0:
        print("ncp")
else:
    print("cp")











    
