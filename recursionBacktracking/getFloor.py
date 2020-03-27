def getFloor(arr,low,high,x):
    if x<arr[low]:
        return -1
    if x>=arr[high]:
        return arr[high]
    mid=(low+high)//2
    if mid==low:
        return arr[mid]
    if arr[mid]==x:
        return arr[mid]
    elif arr[mid]<x:
        return getFloor(arr,mid,high,x)
    else:
        return getFloor(arr,low,mid-1,x)
n=int(input())
arr = list(map(int, input().split()))

find=int(input())
print(getFloor(arr,0,n-1,find))
