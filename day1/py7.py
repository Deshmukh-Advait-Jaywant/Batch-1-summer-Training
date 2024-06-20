'''
inp:
    asd8728#*^A
op:
    if valid then -1

------------------------
ip:
123456789

op:
    3
-----------------------------
ip:
    ab

op:
    6
----------------------
'''
s=input("enter a password")
u,l,s,d=0,0,0,0
for i in s:
    if i.isdigit():
        d=1
    elif i.islower():
        l=1
    elif i.isupper():
        u=1
    else:
        s=1

m=4-(l+d+u+s)
if len(s)+m<8:
    print(8-len(s))
else:
    if m==0:
        print(-1)
    else:
        print(m)



'''
caps=[]
smalls=[]
nums=[]
special=[]
char=-1

for i in s:
    if i.isupper():
        caps.append(i)
    elif i.islower():
        smalls.append(i)
    elif i.isdigit():
        nums.append(i)
    else:
        special.append(i)

if len(s)>=8 and len(caps)!=0 and len(smalls)!=0 and len(nums)!=0 and len(special)!=0:
    print(char)
elif len(s)>8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(smalls)==0:
        char+=1    
    if len(nums)==0:
        char+=1
    if len(special)==0:
        char+=1
    print(char) 
elif len(s)<8:
    char+=1
    if len(caps)==0:
        char+=1
    if len(smalls)==0:
        char+=1    
    if len(nums)==0:
        char+=1
    if len(special)==0:
        char+=1
    if char+len(s)<8:
        char=char+(8-len(s)-char)
    print(char)    
print(caps, smalls,nums,special)
'''
    
    
