def largestRegion(matrix,R,C):
    if len(matrix)==0:
        return 0
    res=0
    finalRes=-1
    for i in range(R):
        for j in range(C):
            cnt=[0]
            if matrix[i][j]==1:
                dfs(matrix,i,j,cnt)
                finalRes=max(finalRes,cnt[0])
    return finalRes

def dfs(matrix,i,j,cnt):
    if i<0 or i>=R or j<0 or j>=C or matrix[i][j]==0:
        return 0
    if matrix[i][j]==1:
        cnt[0]+=1
        matrix[i][j]=0
        dfs(matrix,i-1,j,cnt)
        dfs(matrix, i, j+1,cnt)
        dfs(matrix, i + 1, j,cnt)
        dfs(matrix,i,j-1,cnt)




matrix=[[1,1,1],[0,0,0],[0,1,1]]
R=len(matrix)
C=len(matrix[0])
print(largestRegion(matrix,R,C))