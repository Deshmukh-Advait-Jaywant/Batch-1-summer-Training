def  three(n):
    for i in range(0,len(n)-2):
        for j in range(i+1,len(n)-1):
            for k in range(j+1,len(n)):
                print(n[i],n[j],n[k])
def  threerec(n,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(n)):
            fun(curr+[n[i]],i+1)
        return
    fun([],0)
n=[3,2,5,4,9]
k=3
threerec(n,k)
