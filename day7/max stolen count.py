'''
ip:
    [3,9,4,1,5,7]    Gold in each house
     0 1 2 3 4 5

    if theif stole gold in one house he cant steal in next consecutive house

    find the maxinum amount theif can steal
'''
def findmax(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    left=l[0]+findmax( l[2:])
    right=l[1]+findmax(l[3:])
    return max(left,right)


l=[13,9,4,10,5,7]
print(findmax(l))
        
