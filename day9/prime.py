'''
ip:
    [4,8,14,22,36,68]

    array in increasing order
    all elements in array are non prime numbers

    find largest prime number between two points
    and sum of all those numbers should be the output

'''
def findPrime(m):
    for i in range(2,(m//2)+1):
        if m%i==0:
            return 0
    return m
    

l=[14,16,20,22]

res=[]
for i in range(len(l)-1):
    m=0
    for j in range(l[i],l[i+1]):
        m=max(findPrime(j),m)
    res.append(m)
print(res)    
print(sum(res))
