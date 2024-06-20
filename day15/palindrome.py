def palindrome(num):
    num1=num
    r,rev=0,0
    while num:
        r=num%10
        rev=rev*10+r
        num=num//10
    if num1==rev:
        return True
    return False
'''

i=1
if palindrome(num):
    print("yes")
else:
    while 1:
        if palindrome(num+i):
            print(num+i)
            break
        i+=1
        
'''
num=input("enter num")
if palindrome(int(num)):
    print("yes")
else:
    if len(num)%2==0:
        s1=num[:len(num)//2]
        if s1+s1[::-1]<num:
            s1=str(int(s1)+1)
            rev=s1+s1[::-1]
        rev=s1+s1[::-1]
        print(rev)
    else:
        s1=num[:(len(num)//2)+1]
        if s1+s1[::-1]<num:
            s1=str(int(s1)+1)
            rev=s1+s1[::-1]
        rev=s1+s1[::-1]
        print(rev)
