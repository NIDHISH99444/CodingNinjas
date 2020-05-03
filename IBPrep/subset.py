

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
    for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
        if board[i][j]==1:
            return False

    return True


def nQueenHelper(board,n,row,ll):

    if row>=n:
        res=[]

        for i in range(n):
            str=""
            for j in range(n):
                if board[i][j]==1:
                    str+="Q"
                else:
                    str+='.'
            res.append(str)
        ll.append(res)
        return


    for j in range(n):
        if isPossible(board,n,row,j):
            board[row][j]=1
            nQueenHelper(board,n,row+1,ll)
            board[row][j]=0


def nQueen(n):
    board = [[0 for i in range(n)] for j in range(n)]
    ll=[]
    nQueenHelper(board,n,0,ll)
    return ll
n=4
print(nQueen(n))
