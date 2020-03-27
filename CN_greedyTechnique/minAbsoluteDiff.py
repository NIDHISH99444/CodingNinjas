import sys
def minAbsoluteDiff(arr):
    arr.sort()
    minDiff=sys.maxsize
    for i in range(1,len(arr)):
        minDiff=min(arr[i]-arr[i-1],minDiff)
    return minDiff


n=int(input())
arr=list(map(int,input().split()))
print(minAbsoluteDiff(arr))