'''
ip:
    1.number of queries

        5
        1 school
        1 world
        1 word
        1 scholar
        2 word
        2 wood
        3 sch

if 1- insert the word
    2- search for the word print True if there else print false
    3- search for the word with prifix sch if word is availabe with prefix print True else false
'''
queries=int(input("num of queries"))
lis=[]
res=[]
for i in range(queries):
    n=int(input("enter number"))
    w=input("enter word")
    if n==1:
        if w not in lis:
           lis.append(w)
    elif n==2:
        if w in lis:
            res.append(True)
        else:
            res.append(False)
    elif n==3:
        cnt=0
        l=len(w)
        for i in lis:
            if w==i[:l]:
                cnt+=1
        res.append(cnt)
        '''l=len(w)
        f=0
        for i in lis:
            if w==i[:l]:
                res.append(True)
                f=1
                break
        if f==0:
            res.append(False)'''
    elif n==4:
        lis.remove(w)
for i in res:
    print(i)

    
    
