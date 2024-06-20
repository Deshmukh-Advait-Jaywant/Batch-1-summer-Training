'''
coin exchange
'''

#coins=[2,3,4,5]
#val=17
#with matrix

coins=[2,3,4,6,10]
val=25
dp=[]
for i in range(len(coins)):
    l=[-1]*(val+1)
    dp.append(l)
for i in range(len(coins)):
    for j in range(val+1):
        if coins[i]==j:
            dp[i][j]=1
            continue
        elif coins[i]>j:
            dp[i][j]=dp[i-1][j]
        elif j>coins[i]:
            x=j-coins[i]
            if dp[i][x]==-1:
                if dp[i-1][j]>0:
                    dp[i][j]=dp[i-1][j]
                    continue
                dp[i][j]=-1
            else:
                dp[i][j]=dp[i][x]+1
            
        
for i in range(len(dp)):
    print(dp[i])

                    
    
coins=[2,3,4,6,10]
n=25








    
