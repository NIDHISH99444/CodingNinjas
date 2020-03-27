
def checkProfit(arr):
    minEle=arr[0]
    maxDiff=arr[1]-arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minEle:
            minEle=arr[i]
        elif arr[i]-minEle>maxDiff:
            maxDiff=arr[i]-minEle
    return maxDiff


#n=int(input())
#arr=list(map(int,input().split()))
arr=[62, 63, 70, 66, 64, 68, 61]
print(checkProfit(arr))