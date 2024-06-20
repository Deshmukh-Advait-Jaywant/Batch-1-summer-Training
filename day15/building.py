'''
ip:
    [3,5,9,6,8,10]   these are all the heights of the building

    sun at 6am will be on left side and count the number of building that sun rays will fall
    sun at 6pm will be on right side and count the number of building that sun rays will fall
'''
#l=[3,5,9,6,8,10]
l=[3,4,5,10,4,3]
left=0
lc,rc=1,1
right=len(l)-1
lm=l[left]
rm=l[right]
while left<=len(l) and right>=0:
    if lm<l[left]:
        lm=l[left]
        lc+=1
    if rm<l[right]:
        rm=l[right]
        rc+=1
    left+=1
    right-=1
print(lc,rc)
    
