'''
ip:
    14
op:
    if prime print same number
    else print the next prime number

'''
def prime(n):
    for i in range(2,n//2):
        if n%i == 0:
           return False
    return True
n=8
if prime(n):
    print(n)
else:
    while 1:
        if prime(n+1):
            print(n+1)
            break
        else:
            n+=1
        

        
