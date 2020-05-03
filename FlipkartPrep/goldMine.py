def checkGold(row,col):
    if col>n or col<0:
        return 0
    if row>m or row<0:
        return 0
    x=checkGold(row-1,col+1)
    y=checkGold(row,col+1)
    z=checkGold(row+1,col+1)
    return gold[row][col]+max(x,y,z)


def getMaxGold(gold,m,n):
    maxVal=0
    for j in range(n):
        g=checkGold(j,0)
        maxVal=max(maxVal,g)
    return maxVal


gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m = 3
n = 3

print(getMaxGold(gold, m, n))