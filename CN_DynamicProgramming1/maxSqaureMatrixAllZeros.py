def maxSqaureMatrix(matrix,r,c):
    newMatrix=[[0 for i in range(c)]for j in range(r)]
    for i in range(r):
        if matrix[i][0]==0:
            newMatrix[i][0]=1
        else:
            newMatrix[i][0]=0

    for j in range(1,c):
        if matrix[0][j]==0:
            newMatrix[0][j]=1
        else:
            newMatrix[0][j]=0

    for i in range(1,r):
        for j in range(1,c):
            if matrix[i][j]==0:
                newMatrix[i][j]=min(newMatrix[i-1][j],newMatrix[i-1][j-1],newMatrix[i][j-1])+1
            else:
                newMatrix[i][j]=0

    finalRes=0
    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            if newMatrix[i][j]>finalRes:
                finalRes=newMatrix[i][j]
    return finalRes



#matrix=[[0,0,0,0,1],[0,0,0,0,1],[1,0,0,0,1]]
r,c=list(map(int,input().split()))
matrix=[]
for i in range(r):
    matrix.append(list(map(int,input().split())))
print(maxSqaureMatrix(matrix,r,c))