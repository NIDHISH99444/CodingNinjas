def minCost(matrix,m,n):
    dp=[[0 for i in range(n)] for j in range(m)]
    dp[m-1][n-1]=matrix[m-1][n-1]
    for i in range(m-2,-1,-1):
        dp[i][n-1]=matrix[i][n-1]+dp[i+1][n-1]
    for j in range(n-2,-1,-1):
        dp[m-1][j]=matrix[m-1][j]+dp[m-1][j+1]
    for i in range(m-2,-1,-1):
        for j in range(n-2,-1,-1):
            dp[i][j]=matrix[i][j]+min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])
    print(dp)
    return dp[0][0]



matrix=[[4,3,2],[1,8,3],[1,1,8]]
print(minCost(matrix,len(matrix),len(matrix[0])))