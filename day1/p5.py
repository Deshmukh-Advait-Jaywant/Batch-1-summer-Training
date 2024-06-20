'''
ip:
    300
    400

op: count of numbers divisible by 7 in the give range
'''

a=int(input("enter a"))
b=int(input("enter b"))
count=0
diff=abs(a/7 - b/7)
'''
for i in range(a,b+1):
    if i%7==0:
        count+=1
'''    
print("count",int(diff))
