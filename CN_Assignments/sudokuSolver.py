
def presentInRow(board,row,num):
    for j in range(9):
        if board[row][j]==num:
            return True
    return False

def presentInColumn(board,col,num):
    for i in range(9):
        if board[i][col]==num:
            return True
    return False

def presentInBox(board,row,col,num):
    for i in range(row,row+3):
        for j in range(col,col+3):
            if board[i][j]==num:
                return True
    return False

def isPossible(board,row,col,num):
    if presentInRow(board,row,num):
        return False
    if presentInColumn(board,col,num):
        return False
    if presentInBox(board,row-(row%3),col-(col%3),num):
        return False
    return True

def solveSudoku(board):
    row=-1
    col=-1
    flag=False
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row=i
                col=j
                flag=True
                break
        if flag is True:
            break
    if row==-1:
        return True
    for num in range(1,10):
        if isPossible(board,row,col,num):
            board[row][col]=num
            if solveSudoku(board) is True:
                return True
            board[row][col]=0
    return False




board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
#
# 9 0 0 0 2 0 7 5 0
# 6 0 0 0 5 0 0 4 0
# 0 2 0 4 0 0 0 1 0
# 2 0 8 0 0 0 0 0 0
# 0 7 0 5 0 9 0 6 0
# 0 0 0 0 0 0 4 0 1
# 0 1 0 0 0 5 0 8 0
# 0 9 0 0 7 0 0 0 4
# 0 8 2 0 4 0 0 0 6