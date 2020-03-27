# def printFinal(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             print(matrix[i][j],end=" ")
#     print()
def ratMazeUtil(matrix,solution,x,y,n):
    if  x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        solution[x][y]=0
        return
    if x<0 or x>=n or y<0 or y>=n or matrix[x][y]==0 or solution[x][y]==1:
        return
    solution[x][y]=1
    ratMazeUtil(matrix,solution,x,y-1,n)
    ratMazeUtil(matrix, solution, x-1, y,n)
    ratMazeUtil(matrix, solution, x, y+1,n)
    ratMazeUtil(matrix, solution, x+1,y,n)
    solution[x][y]=0

def ratMaze(matrix,n):
    solution=[[0 for i in range(n)]for j in range(n)]
    ratMazeUtil(matrix,solution,0,0,n)
#
# matrix=[]
# n=int(input())
# for i in range(n):
#     ll=[int(j) for j in input().split()]
#     matrix.append(ll)

matrix=[[1,1,0],[1,1,0],[1,1,1]]
ratMaze(matrix,len(matrix))