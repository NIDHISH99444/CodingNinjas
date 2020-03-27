# def coinChange(coinSum,denomination,numD,matrix):
#     if coinSum==0:
#         return 1
#     if coinSum<0:
#         return 0
#     if len(denomination)==0:
#         return 0
#     if matrix[coinSum][numD]!=-1:
#         return matrix[coinsum][numD]
#     first=coinChange(coinSum-denomination[0],denomination,numD,matrix)
#     second=coinChange(coinSum,denomination[1:],numD-1,matrix)
#     matrix[coinSum][numD]=first+second
#     return first+second



def coinChange(coinsum,matrix):
    for i in range(1,numD+1):
        for j in range(1,coinsum+1):
            if i>j:
                matrix[i][j]=matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-denomination[i-1]]
    return matrix[-1][-1]


numD=int(input())
denomination=list(map(int,input().split()))
coinsum=int(input())

matrix=[[0 for i in range(coinsum+1)]for j in range(numD+1)]

for i in range(numD+1):
    matrix[i][0]=1

print(coinChange(coinsum,matrix))