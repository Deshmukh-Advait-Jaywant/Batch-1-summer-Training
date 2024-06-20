'''
ip:
    12321
op:
/    palindrome or not
=
'''
'''
def reverse(num,rev):
    if num==0:
        return rev
    
    rem=0
    rem=num%10
    rev=rev*10+rem
    return reverse(num//10,rev)

num=int(input())
rev=reverse(num,0)

if rev==num:
    print('palindrome')
else:
    print("not palindrome")
'''

'''
ip:
    5 3 2 7 8 4
    m t w t  f  s

max profit made
buy and sell a pen

'''
'''
l=[9,8,7,6,5,4]
maximum=0
profit=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            profit=l[j]-l[i]
        if maximum<profit:
            maximum=profit
print(maximum)

'''

'''
l=[5,4,3,2,1]
maximum=0
profit=0
b=99999999999
for i in range(len(l)-1):
    if b>l[i]:
        b=l[i]
    else:
        profit=l[i]-b
        if maximum<profit:
            maximum=profit
print(maximum)
'''

'''
ip=5
op:
    *  * *  *  *
    * 1 2 3  *
    * 4 5 6  *
    * 7 8 9  *
    *  * *  *  *
'''
'''
n=int(input())
x=1
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print('*',end=" ")
        else:
            print(x ,end=" ")
            x+=1
    print()

'''

'''
ip:
    4
op:
    - - - - a - - - -
    - - - a b a - - -
    - - a b c b a - -
    - a b c d c b a -
'''
n=int(input())
ch=97
for i in range(n):
    for j in range(n-i):
        print("-",end="")
        for x in range(i):
            print(chr(ch))
    print()









