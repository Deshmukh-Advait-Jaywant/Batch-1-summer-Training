'''
Give a binary matrix with 1's and 0's
1's ----> trees
0's-----> land
l[r][c] is the starting index of fire

fire moves in top, down,left, right only
i/p:
1 0 0 1
1 0 0 0
1 0 1 0
0 1 1 1

r=0
c=0

o/p:
the output is 5

i/p:
1 0 0 1
1 0 0 1
1 1 1 0
0 1 1 1

r=0
c=0

o/p:
the output is 2
'''
l=[[1,1,1,1,1,1],[0,1,0,1,1,0],[1,1,1,1,0,1],[0,1,1,1,1,1],[1,1,0,1,0,1],[1,1,1,1,1,0]]
n=len(l)
count=0
i=0
j=0
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    
    if l[i][j]==1:
        l[i][j]=0    
    
    if i>0:
        fun(l,i-1,j,n) #Top
    if i<n-1:
        fun(l,i+1,j,n) #Bottom  
    if j>0:
        fun(l,i,j-1,n) #left
    if j<n-1:
        fun(l,i,j+1,n) #right

if l[i][j]==1:
    print(l[i][j])
    fun(l,i,j,n)
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
print(count)
