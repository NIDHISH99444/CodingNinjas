def problemDiscussion(arr,k):
    arr.sort()
    n=len(arr)
    maxDiff=arr[n-1]-arr[0]
    big=arr[n-1]-k
    small=arr[0]+k
    if small>big:
        small,big=big,small
    for i in range(1,len(arr)-1):
        add=arr[i]+k
        sub=arr[i]-k
        if sub>=small or add<=big:
            continue
        elif big-sub<=add-small:
            small=sub
        else:
            big=add
    return min(maxDiff,big-small)

n,k=list(map(int,input().split()))
arr=list(map(int,input().split()))
print(problemDiscussion(arr,k))
