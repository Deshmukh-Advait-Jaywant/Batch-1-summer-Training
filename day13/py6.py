'''
ip:
    14
op:
    if prime print same number
    else print the next prime number

'''

def prime(n):
    for i in range(2,(n//2)+1):
        if n%i == 0:
           return False
    return True
'''
n=int(input("enter a number")
if prime(n):
    print(n)
else:
    while 1:
        if prime(n+1):
            print(n+1)
            break
        else:
            n+=1
'''
#NUMBER OF PRIME DIGITS
n=3572
count=0
while n:
    if n%10 in [2,3,5,7]:
        count=count+1
    n=n//10
print(count)
'''
while n:
    x=n%10
    if prime(x):
        count+=1
    n=n//10
'''

