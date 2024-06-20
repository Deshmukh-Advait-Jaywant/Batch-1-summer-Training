'''
input :
    2 5 7 9
    1 3 6 7 10 13

output :
    1 2 3 5 6 7 7 9 10 13
'''
#method 1
'''
list1=[2,5,7,9]
list2=[1,3,6,7,10,13]

for i in list2:
    list1.append(i)
list1.sort()

print(list1)
'''

#method2
list1=[2,5,7,9]
list2=[1,3,6,7,10,13]
res=[]
i,j=0,0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        res.append(list1[i])
        i+=1
    else:
        res.append(list2[j])
        j+=1

if i!=len(list1):
    res.extend(list1[i:])
    '''l=list1[i:]
     for i in l:
         res.append(l)
         '''
if j!=len(list2):
  res.extend(list2[j:])
print(res)









      
