'''
ip:

given an list where we are given unlimited coins
[1,2,3,4]

and now you need to make 15rupees using these coins
op:
print the minimum number of coins to make 15
.i.e.
4

'''

coins=[4,3,7]
s=16
c=0
while s:
    for i in range(len(coins)-1,-1,-1):
        if s in coins:
            s=s-s
            c+=1
            break
        if s>coins[i]:
            s-=coins[i]
            c+=1
            break
        else:
            continue
print(c)
