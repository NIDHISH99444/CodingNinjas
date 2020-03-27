def sumArray(arr):
    if len(arr)==0:
        return 0
    return arr[0]+sum(arr[1:])

print(sumArray([]))