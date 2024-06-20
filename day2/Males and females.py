s="MMF"
cm,cf=0,0
for i in s:
    if i=='M':
        cm+=1
    else:
        cf+=1
print(cm,cf)
if cf==cm:
    print(0)
elif cf>cm:
    print("F")
else:
    print("M")

