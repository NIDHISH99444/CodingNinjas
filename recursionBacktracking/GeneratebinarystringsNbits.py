def generateString(arr, low ,high):
    if low ==high :
        printArray(arr,high)
        return
    else:
        arr[low]=0
        generateString(arr,low+1,high)
        arr[low] = 1
        generateString(arr, low + 1, high)

def printArray(arr,high):
    for i in range(high):
        print(arr[i],end=" ")
    print()
high=3
arr=[None]*high
generateString(arr,0,high)