'''
ip:
    3
    
     x y z
     p q r
     a b c

    "xpaypb"
op:
    yes
'''
  
def m(matrix,s,a):
    for i in range(len(s)):
        if s[i] not in matrix[i%a]:
            return 'no'
        else:
            matrix[i].remove(s[i])
    return 'yes'
a=int(input("enter a max size"))
matrix = []
s=input("enter the string")
for i in range(a): 
    l =[] 
    for j in range(a):
         l.append(list(input()))
    matrix.append(l)
print(m(matrix,s,a))

     
