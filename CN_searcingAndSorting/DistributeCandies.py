def canDistributeCandies(arr,mid,people):
    count=0
    for i in range(len(arr)):
        count+=arr[i]//mid
        if count>=people:
            return True

    return False


def distributeCandies(arr,people):
    end=max(arr)
    start=0
    while start<=end:
        mid=start+(end-start)//2
        if canDistributeCandies(arr,mid,people):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans

n=int(input())
for i in range(n):
    boxes,people=list(map(int,input().split()))
    chocolateInEachBox=list(map(int,input().split()))
    print(distributeCandies(chocolateInEachBox,people))
