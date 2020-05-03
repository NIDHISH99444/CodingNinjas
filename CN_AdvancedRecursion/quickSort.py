# Sort an array A using Quick Sort.
# Change in the input array itself. So no need to return or print anything.
# Input format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)
# Output format :
# Array elements in increasing order (separated by space)
# Constraints :
# 1 <= n <= 1000
# Sample Input:
# 6
# 2 6 8 5 4 3
# Sample Output:
# 2 3 4 5 6 8

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