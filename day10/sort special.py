'''
ip:
    [4,9,8,2,14,3,5,6]
    take first three elements
    unsorted array

    4 8 9 2 14 3 5 6
       2 8 9 14 3 5 6
          8 9 14 3 5 6
            3  9 14 5 6
                 5  9 14 6
                     6 9 14
    4 2 8 3 5 6 9 14               
    (4,8,9)  (2,14,22)    ............

'''     
l=[4,9,8,2,14,3,5,6]
res=[]
for i in range(len(l)-2):
    l[i]=min(l[i],l[i+1],l[i+2])
    l[i+2]=max(l[i],l[i+1],l[i+2])
    l[i+1]=sum([l[i],l[i+1],l[i+2]])-l[i]-l[i+2]
print(l)
