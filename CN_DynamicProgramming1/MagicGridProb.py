def magicGridProb(matrix,r,c):
    matrix[r-1][c-1]=1
    for i in range(c-2,-1,-1):
        matrix[r-1][i]=matrix[r-1][i+1]-matrix[r-1][i]
        if matrix[r-1][i]<=0:
            matrix[r-1][i]=1

    for j in range(r-2,-1,-1):
        matrix[j][c-1]=matrix[j+1][c-1]-matrix[j][c-1]
        if matrix[j][c-1]<=0:
            matrix[j][c-1]=1

    for  i in range(r-2,-1,-1):
        for j in range(c-2,-1,-1):
            matrix[i][j]=min(matrix[i+1][j],matrix[i][j+1])-matrix[i][j]
            if matrix[i][j]<=0:
                matrix[i][j]=1
    return matrix[0][0]


p=int(input())

for i in range(p):
    matrix = []
    m,n=list(map(int,input().split()))
    for i in range(m):
        matrix.append([int(x) for x in input().split()])
#print(matrix)
    print(magicGridProb(matrix,m,n))
#matrix=[[0,-2,-3,1],[-1,4,0,-2],[1,-2,-3,0]]
#print(magicGridProb(matrix,len(matrix),len(matrix[0])))