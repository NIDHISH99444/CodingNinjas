import math
def canPlace(grid,n,row,col,currNumber):
    if grid[row][col]!=0:
         return False
    rootn=math.sqrt(n)
    for x in range(0,n):
        if grid[row][x]==currNumber:
            return False
        if grid[x][col]==currNumber:
            return False
    boxRow=int(row//rootn)
    boxCol=int(col//rootn)
    boxStartCellRow=int(boxRow*rootn)
    boxStartCellCol=int(boxCol*rootn)
    for i in range(int(boxStartCellRow),int(boxStartCellRow+rootn)):
        for j in range(int(boxStartCellCol),int(boxStartCellCol+rootn)):
            if grid[i][j]==currNumber:
                return False

    return True
def sudokuSolver(grid,n,row,col):
    if row==n:
        print(grid)
        return True
    if col==n:
        sudokuSolver(grid,n,row+1,0)
    if grid[row][col] != 0:
        return True
    for curNumber in range(1,n+1):
        if canPlace(grid,n,row,col,curNumber):
            grid[row][col]=curNumber
            if sudokuSolver(grid,n,row,col+1):
                return True
                grid[row][col]=0

    return False
# grid=[
#     [0,2,3,4],
#     [4,3,2,0],
#     [3,4,0,2],
#     [2,0,4,3]]
n=int(input())
row=[]
for i in range(n):
    row.append(list(map(int,input().split())))


print(sudokuSolver(row,n,0,0))