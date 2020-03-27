def largestPiece(matrix,i,j):


    if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]=='0':
        return
    if matrix[i][j] == '1':
        matrix[i][j] = '0'
        cnt[0] += 1
    largestPiece(matrix,i,j-1)
    largestPiece(matrix,i-1,j)
    largestPiece(matrix,i,j+1)
    largestPiece(matrix,i+1,j)



matrix=[]
n=int(input())
for i in range(n):
    m=input()
    ll=[char for char in m]
    matrix.append(ll)

maxCount=0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]=='1':
            cnt = [0]
            largestPiece(matrix,i,j)
            maxCount=max(maxCount,cnt[0])
print(maxCount)