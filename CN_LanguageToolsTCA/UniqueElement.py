def uniqueElement(arr):
    sum=0
    for i in range(len(arr)):
        sum^=arr[i]
    return sum

print(uniqueElement([2 ,3 ,1 ,6 ,3 ,6, 2]))