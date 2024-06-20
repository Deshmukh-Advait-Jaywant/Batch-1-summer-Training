'''
coin exchange when jou have 1 coin for each value
'''

#coins=[2,3,4,5]
#val=17
#with matrix

coins=[2,3,5,6]
val=11
dp=[]
s=[]
for i in range(len(coins)):
    l=[0]*(val+1)
    dp.append(l)
for i in range(len(coins)):
    dp[i][0]=1
for i in range(len(coins)):
    for j in range(val+1):
        if coins[i]==j:
            dp[i][j]=1
            continue
        elif coins[i]>j:
            dp[i][j]=dp[i-1][j]
        if j>coins[i]:
            x=j-coins[i]
            if dp[i][x]==0:
                if dp[i-1][j]>0:
                    dp[i][j]=dp[i-1][j]
                    continue
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][x]
       
for i in range(len(dp)):
    print(dp[i])

                    
    
coins=[2,3,4,6,10]
n=25








    
