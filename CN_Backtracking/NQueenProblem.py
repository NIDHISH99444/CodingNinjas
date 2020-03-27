def isPossible(board,n ,row,col):
    #Checking same column
    for i in range(row-1,-1,-1):
        if board[i][col]==1:
            return False
    #Checking upper diagonal on left side
    for i,j in  zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if board[i][j]==1:
            return False
    #checking uper diagonal on right side
    for i,j in zip(range(row-1,-1,-1),range(col+1,n,1)):
        if board[i][j]==1:
            return False

    return True


def nQueenHelper(board,n,row):
    if row>=n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
        print()
        return
    for j in range(n):
        if isPossible(board,n,row,j):
            board[row][j]=1
            nQueenHelper(board,n,row+1)
            board[row][j]=0


def nQueen(n):
    board = [[0 for i in range(n)] for j in range(n)]
    nQueenHelper(board,n,0)
n=int(input())
nQueen(n)