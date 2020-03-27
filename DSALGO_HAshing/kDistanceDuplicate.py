def duplicateKDistance(arr,k):
    newArr=[]

    for i in range(len(arr)):
        if arr[i] in newArr:
            return True
        else:
            newArr.append(arr[i])
        if i>=k:
            newArr.remove(arr[i-k])
    return False


print(duplicateKDistance([1, 2, 3, 4, 1, 2, 3, 4],3))
