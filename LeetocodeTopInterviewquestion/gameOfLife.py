

def checkLives(matrix,i,j):
    dir=[[0,-1],[0,1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    res=0
    for  k in range(len(dir)):
        newRow=i+dir[k][0]
        newCol=j+dir[k][1]

        if newRow>=0 and newRow<len(matrix) and newCol>=0 and newCol<len(matrix[0]) and ( matrix[newRow][newCol]==1 or matrix[newRow][newCol]==2):
            res+=1
    return res

def update(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==-1:
                matrix[i][j]=1
            if matrix[i][j]==2:
                matrix[i][j]=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()
def gameOfLife(matrix):
    #live->death  (2)
    #death -> live (-1)
    #update finally 2->0 ,1->-1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                lives=checkLives(matrix,i,j)
                if lives<2 or lives>3:
                    matrix[i][j]=2
            if matrix[i][j]==0:
                lives=checkLives(matrix,i,j)

                if lives==3:
                    matrix[i][j]=-1

    update(matrix)

matrix=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

gameOfLife(matrix)