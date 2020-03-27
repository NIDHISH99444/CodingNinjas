def subsetSum(subset,sum):
    m=len(dp)
    n=len(dp[0])

    for i in range(m):
        dp[i][0]=1
    for i in range(1,m):
        for j in range(1,n):
            if i> j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-subset[i-1]]


    return dp[-1][-1]
n=int(input())
subset=list(map(int,input().split()))
sum=int(input())
dp=[[0 for i in range(sum+1)]for j in range(len(subset)+1)]

if subsetSum(subset,sum):
    print("Yes")
else:
    print("No")