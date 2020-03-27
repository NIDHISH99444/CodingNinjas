def firstIndex(arr,x,count=0):
    if len(arr)==0:
        return -1

    count += 1
    return firstIndex(arr[1:],x,count)
    if arr[-1]==x:
        return count

print(firstIndex([9,8,10,8,9],8))