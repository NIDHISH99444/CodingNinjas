
# def checkArraySorted(arr):
#     if len(arr)==1:
#         return True
#     if arr[0]<=arr[1]:
#         return checkArraySorted(arr[1:])
#     return False
def checkArraySorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

n=list(map(int,input().split()))
print(checkArraySorted(n))