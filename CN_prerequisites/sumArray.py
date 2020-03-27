def sumArray(arr):
    sum=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==0 or j==0 or i==j or i==len(matrix)-1 or j==len(matrix[0])-1 or i+j==len(matrix)-1:
                sum+=arr[i][j]
    print(sum)


matrix=[]
n=int(input())
for i in range(n):
    matrix.append(list(map(int,input().split())))
sumArray(matrix)