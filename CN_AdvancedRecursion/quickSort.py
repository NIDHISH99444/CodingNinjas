def partition(arr,left,right):
    i = (left - 1)  # index of smaller element
    pivot = arr[right]  # pivot

    for j in range(left, right):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return (i + 1)

def quickSort(arr,left,right):
    if left<right:
        par=partition(arr,left,right)
        quickSort(arr,left,par-1)
        quickSort(arr,par+1,right)


#n = int(input())
#arr = list(int(i) for i in input().strip().split(' '))
arr=[2,1,3,4,8,5,7,6]
quickSort(arr, 0, 7)
print(*arr)