'''
ip:
aaabbaaaaddd

op:
a3b2a4d3
'''

s="aaabbaaaadddb"
res=""
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        res=res+s[i]
        res=res+str(count)
        count=1
res=res+s[-1]
res=res+str(count)

print(res)
