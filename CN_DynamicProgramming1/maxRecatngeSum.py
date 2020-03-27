import sys
def kadane(sum):
    msf=-sys.maxsize
    meh=0
    for i in range(len(sum)):
        meh+=sum[i]
        if meh>msf:
            msf=meh
        if meh<0:
            meh=0

    return msf
def maximumRectange(matrix,m,n):

    finalRes=-sys.maxsize
    for i in range(n):
        sum = [0] * m
        for j in range(i,n):
            for k in range(m):
                sum[k]+=matrix[k][j]
            temp=kadane(sum)
            finalRes=max(finalRes,temp)
    return finalRes



# matrix=[]
# m,n=list(map(int,input().split()))
# for i in range(m):
#     matrix.append([int(x) for x in input().split()])
# print(matrix)
matrix=[[-1,-2,-2,-2],[-5,-4,-1,-9],[-3,-2,-6,-3],[-4,-3,-3,-2]]
m,n=4,4
print(maximumRectange(matrix,m,n))