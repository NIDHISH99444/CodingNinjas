def stairCase(n):
    arr[0]=1
    arr[1]=1
    arr[2]=2
    for i in range(3,n+1):
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
    return arr[n]

n=4
arr=[0]*(n+1)
print(stairCase(n))
