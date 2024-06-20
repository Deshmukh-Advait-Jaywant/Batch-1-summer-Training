def fun(matrix,key,i,j,n,lis,flag):
    if matrix[i][j] not in key:
         return
    
    if matrix[i][j] in key:
        lis.append(matrix[i][j])
        l="".join(map(str,lis))
        matrix[i][j]='0'
        print(l)
        if key==l:
            flag=1
    if flag==1:
        print("yes") 
    if i>0:
        fun(matrix,key,i-1,j,n,lis,flag) #Top
    if i<n-1:
        fun(matrix,key,i+1,j,n,lis,flag) #Bottom
    if j>0:
        fun(matrix,key,i,j-1,n,lis,flag) #left
    if j<n-1:
        fun(matrix,key,i,j+1,n,lis,flag) #right
        lis.pop()

n=4        
matrix=[['a','o','s','q'],
             ['e','p','a','r'],
             ['f','a','e','t'],
             ['r','t','l','n']]
key="eat"
for i in range(n):
    for j in range(n):
        if matrix[i][j]==key[0]:
            fun(matrix,key,i,j,n,[],0)
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()
