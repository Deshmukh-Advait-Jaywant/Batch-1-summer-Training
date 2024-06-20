l=7
lis=[0,5,3,6,7,2,1]
'''
lis.sort()
for i in range(len(lis)):
    if lis[i]!=i:
        print(i)
        break
        
'''    
sL=(l*(l+1))//2
for i in lis:
    sL-=i
print(sL)
