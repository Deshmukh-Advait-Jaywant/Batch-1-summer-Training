class node:
    def __init__(self):
        self.d={}
        self.flag=0

class tries:
    def __init__(self):
        self.root=node()
    def insert(self,string):
        t=self.root
        for i in string:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,string):
        t=self.root
        f=1
        for i in string:
            if i in t.d:
                t=t.d[i]
            else:
                print("not found")
                f=0
                break
        if t.flag==1 and f==1:
            print("found")
        else:
            print("not found")
    def prefix(self,string):
        t=self.root
        f=1
        for i in string:
            if i in t.d:
                t=t.d[i]
            else:
                print("not present")
                f=0
                break
        if f==1:
            print("present")
    def printAllPrifix(self,string):
        def fun(t,s):
            if t.flag==1:
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in string:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
    def printLongestPrifix(self,string):
        def fun(t,s,res):
            if t.flag==1:
                res.append(s)
                return res
            for i in t.d:
                res=fun(t.d[i],s+i,res)
            return res
        t=self.root
        s=""
        for i in string:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        res=fun(t,s,[])
        return res
            
t1=tries()
t1.insert("word")
t1.insert("words")
t1.insert("woo")
t1.insert("world")
t1.insert("appleiw")
'''t1.search("apple")
t1.prefix("hi")
'''
t1.printAllPrifix("ap")
pr=["wo","ap"]
m=0
for i in pr:
    x=t1.printLongestPrifix(i)
    #m=max(m,x)
    for j in x:
        if m<len(j):
            m=len(j)
            r=j
            pr=i
print()
print()
print(r,i)
