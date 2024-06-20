class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def addback(self,val):
        if self.head==None:
            self.head=node(val)
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            new=node(val)
            temp.next=new
    def addfront(self,val):
        if self.head==None:
            self.head=node(val)
        else:
            new=node(val)
            new.next=self.head
            self.head=new
    def search(self,val):
        if self.head==None:
            return None
        else:
            temp=self.head
            while temp!=None:
                if temp.val==val:
                    return True
                temp=temp.next
            return False
    def add_in_middle(self,val):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        new=node(val)
        new.next=slow.next
        slow.next=new
    def middleNode(self):
        if self.head==None:
            return None
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.val
    def possiblePairs(self):
        if self.head==None:
            return None
        else:
            temp=self.head
            tp=self.head.next
            while temp.next:
                while tp:
                    print('(',temp.val,tp.val,')',end="  ")
                    tp=tp.next
                temp=temp.next
                tp=temp.next
                print()
    def bubbleSort(self):
        if self.head==None:
            return None
        else:
            end=None
            while end!=self.head:
                p=self.head
                while p.next!=end:
                    q=p.next
                    if p.val>q.val:
                        p.val,q.val=q.val,p.val
                    p=p.next
                end=p
            '''
            t1=self.head
            c=0
            while t1:
                c+=1
                t1=t1.next                
            t1=self.head
            t2=self.head.next
            t=self.head
            temp=0
            for i in range(c):
                while t1.next and t2:
                    if t1.val>t2.val:
                        t1.val,t2.val=t2.val,t1.val
                    t1=t1.next
                    t2=t2.next
                t1=self.head
                t2=self.head.next
                '''
    def evenodd(self):
        tp=self.head
        l=self.head
        while l.next:
            l=l.next
        last=l
        temp=0
        #print(last.val,l.val)
        while tp!=l:
            if tp.val%2!=0:
                if tp==self.head:
                   self.head=self.head.next
                   t=tp
                   tp=tp.next
                   temp=t.val
                   t.next=None
                   new=node(temp)
                   last.next=new
                   last=last.next
                else:
                    op=tp
                    t=self.head
                    while t.next!=tp:
                        t=t.next
                    tp=tp.next
                    t.next=op.next
                    temp=op.val
                    op.next=None
                    new=node(temp)
                    last.next=new
                    last=last.next
                    #print(t.val)
                    #print(tp.val)
                    #print(op.val)
            else:
                tp=tp.next
        if l.val%2!=0:
            if l!=self.head:
                op=tp
                t=self.head
                temp=0
                while t.next!=tp:
                    t=t.next
                tp=tp.next
                temp=op.val
                t.next=op.next
                op.next=None
                new=node(temp)
                last.next=new
                last=last.next
            else:
                t=tp
                self.head=self.head.next
                tp=tp.next
                temp=0
                temp=t.val
                t.next=None
                new=node(temp)
                last.next=new
                last=last.next
                
            

    def display(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
    
        

l=[3,2,4,5,7,8,1]
a=sll()
for i in l:
    a.addback(i)
#a.add_in_middle(0)
#print(a.search(1))
a.display()
print()
a.evenodd()
a.display()
