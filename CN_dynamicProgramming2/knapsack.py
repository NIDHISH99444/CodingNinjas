def knapsack(wt,val):
    m=len(wt)+1
    n=totalWeight+1
    for i in range(1,m):
        for j in range(1,n):
            if j<wt[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
    return dp[-1][-1]


n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
totalWeight=int(input())
# wt=[1,2,4,5]
# val=[5,4,8,6]
# totalWeight=5
dp=[[0 for i in range(totatrlWeight+1)]for j in range(len(wt)+1)]
print(knapsack(wt,val))


