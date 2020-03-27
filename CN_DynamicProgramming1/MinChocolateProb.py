def minChocolates(arr):
    newArr=[1]*len(arr)
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            newArr[i]=newArr[i-1]+1
    for j in range(len(arr)-2,-1,-1):
        if arr[j]>arr[j+1] and newArr[j]<=newArr[j+1]:
            newArr[j]=newArr[j+1]+1
    print( newArr)
    return sum(newArr)


n=list(map(int,input().split()))
if len(n)>1:
    arr=n[1:]
else:
    arr=list(map(int, input().split()))
print(minChocolates(arr))
