'''
ip:

    school
    3

    L 2 ----> hoolsc
    R 3 ----> oolsch
    L 1 ----> chools

    hoc

    school substring:

    sch   cho   hoo   ool

now check hoc is anagram of any substring of school

'''

s="advait"
n=2
lis=[]
s1=""
s2=""
for i in range(n):
    d=input()
    r=int(input())
    if d=='L':
        s1+=s[r]
    else:
        s1+=s[-r]
print(s1)
f=1
li=list(s1)
li.sort()
key=""
for i in li:
    key+=i
print(key)
for i in range(len(s)-n+1):
    t=list(s[i:n+i])
    t.sort()
    lis.append(t)
    
print(lis)
reslis=[]
for i in lis:
    st=""
    for j in i:
        st+=j
    reslis.append(st)
print(reslis)
if key in reslis:
    print("yes")
    f=0
if f==1:
    print("no")
        
