'''
add all digits of number and check sum value if prime print number else print the next number and so on
'''
def fun(x):
    ps=sumNum(x)
    while ps>10:
        ps=sumNum(ps)
    if ps in [2,3,5,7]:
        print(x)
    else:
        x=x+1
        fun(x)
    
def sumNum(n):
    rem=0
    s=0
    while n:
        rem=n%10
        s=s+rem
        n=n//10
    return s
x=int(input("enter number"))
fun(x)


    





