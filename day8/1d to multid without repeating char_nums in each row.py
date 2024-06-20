'''
ip:
    [1,2,3,4,1,2,3,1,2]

op:

    [[1,2,3,4],[1,2,3],[1,2]]
'''

l=[2,3,5,1,2,4,9,1,2,4]
res=[]
s=[]
while l:
    for i in l:
        if i not in s:
            s.append(i)
    for i in s:
        l.remove(i)
    res.append(s)
    s=[]
print(res)

