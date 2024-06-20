'''
given 2 lists
2 list have even and odd numbers

[6,3,2,9,4,7]
[8,9,5,3,6,9]

size of both list are same

generate another list such that an even form 1st list is mappend to all odd numbsers in 2nd list

op:
[6+9,6+5,6+3,6+9,  .. . . . . ..  . .. . . .]=[13,11,9,15 .. .... . . . .. ]
[13,11,9,15,9,7,5,11,11,9,7,13]
'''

def fun(i,j,res,length):
    if i==length:
        return res
    if j==length :
        return fun(i+1,0,res,length)
        
    
    if l1[i]%2==0 and l2[j]%2!=0:
        res.append(l1[i]+l2[j])
    return fun(i,j+1,res,length)
    return res
def fun1(i,j,res,length,s):
    if i==length:
        return res
    if j==length :
        if s:
            res.append(sum(s))
            s=[]
        return fun1(i+1,0,res,length,[])
    if l1[i]%2==0 and l2[j]%2!=0:
        s.append(l1[i]+l2[j])
    return fun1(i,j+1,res,length,s)
    return res
l1=[6,3,2,9,4,7]
l2=[8,9,5,3,6,9]
le1,le2=len(l1),len(l2)
i,j=0,0
'''res=[]
while le1:
    le2=len(l2)
    j=0
    while le2:
        if l1[i]%2==0 and l2[j]%2!=0:
            res.append(l1[i]+l2[j])
        j+=1
        le2-=1
    i+=1
    le1-=1'''
#print(fun(0,0,[],le1))
print(fun1(0,0,[],le1,[]))
