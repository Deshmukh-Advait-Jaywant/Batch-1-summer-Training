'''
print yes if we can show a number as sum of prime numbers
else
print no
'''
def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
def sumOfprime(nums):
    for i in range(2,nums):
        if prime(i) and prime(nums-i):
            return True
    return False
    
num=int(input("enter  "))
print(sumOfprime(num))
