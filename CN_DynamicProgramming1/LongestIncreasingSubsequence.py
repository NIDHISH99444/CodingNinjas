def longestIncreasingSequence(arr):
    newArr=[1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]<arr[i]:
                newArr[i]=max(newArr[i],newArr[j]+1)
    print(newArr)
    return max(newArr)

def longestDecreasingSequence(arr):
    newArr=[1]*len(arr)
    for i in range(len(arr)-2,-1,-1):
        for j in range(len(arr)-1,i,-1):
            if arr[i]>arr[j]:
                newArr[i]=max(newArr[i],newArr[j]+1)
    print(newArr)
    return max(newArr)

print(longestIncreasingSequence([4,3,9,7,6,8, 20]))
print(longestDecreasingSequence([4,3,9,7,6,8, 20]))

