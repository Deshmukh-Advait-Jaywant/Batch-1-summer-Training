class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root==None:
            self.root=node(data)
        else:
            self.recInsert(self.root,data)
    def recInsert(self,root,data):
        if data>root.data:
            if root.right is None:
                root.right=node(data)
            else:
                self.recInsert(root.right,data)
        else:
            if root.left is None:
                root.left=node(data)
            else:
                self.recInsert(root.left,data)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end="->")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end="-> ")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end="->")
    def search(self,root,data):
        if root is None:
            return
        if root.data==data:
            return root.data
        if data>root.data:
            return self.search(root.right,data)
        else:
            return self.search(root.left,data)
    def sumOfnodes(self,root):
        if root==None:
            return 0
        return self.sumOfnodes(root.left)+self.sumOfnodes(root.right)+root.data
    def evenSum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return self.evenSum(root.left) + self.evenSum(root.right)+root.data
        else:
            return self.evenSum(root.left) + self.evenSum(root.right)
    def oddSum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return self.oddSum(root.left) + self.oddSum(root.right)
        else:
            return self.oddSum(root.left) + self.oddSum(root.right)+root.data
    def diffEvenOdd(self,root,ev,od):
        if root==None:
            return 0
        #return self.evenSum(root)-self.oddSum(root)
        if root.data%2==0:
            return self.diffEvenOdd(root.left,ev,od) + self.diffEvenOdd(root.right,ev,od)+root.data
        else:
            return self.diffEvenOdd(root.left,ev,od) + self.diffEvenOdd(root.right,ev,od)-root.data
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left), self.height(root.right))+1
    def checkBalanceOrnot(self,root):
        if root==None:
            return -1
        return abs(self.height(root.left)-self.height(root.right))<=1
    def NoOfLeaf(self,root):
        if root is None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.NoOfLeaf(root.left)+self.NoOfLeaf(root.right)
    def sumOfLeafNode(self,root):
        if root is None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.sumOfLeafNode(root.left)+self.sumOfLeafNode(root.right)
    def depth(self,root,data,c):
        if root==None:
            return -1
        if root.data==data:
            return c
        if root.data>data:
            return self.depth(root.left,data,c+1)
        else:
            return self.depth(root.right,data,c+1)

x=tree()
l=[3,9,20,15,7]
for i in l:
    x.insert(i)
#x.display()

print()

print()
x.preorder(x.root)
'''
print()
x.postorder(x.root)
print()
x.inorder(x.root)
print()
print(x.sumOfnodes(x.root.left))
print()'''

print(x.evenSum(x.root))
print()
#print(x.oddSum(x.root))

#print(abs(x.diffEvenOdd(x.root,0,0)))
#print(x.height(x.root))
if x.checkBalanceOrnot(x.root) :
    print("yes")
else:
    print("no")
#print(x.NoOfLeaf(x.root))
    '''
print(x.sumOfLeafNode(x.root))
if x.search(x.root,21):
   print("yes")
else:
    print("no")'''
print(x.depth(x.root,20,0))
