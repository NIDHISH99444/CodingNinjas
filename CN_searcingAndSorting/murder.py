def merge(arr,left,mid,right):
    i=left
    j=mid
    k=0
    count=0
    temp=[0]*(right-left+1)
    while i<mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            count += arr[i] * (right - j + 1)
            i+=1
            k+=1

        else:
            temp[k]=arr[j]
            j+=1
            k+=1

    while i <mid :
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<=right:
        temp[k]=arr[j]
        k+=1
        j+=1
    p=0
    for s in range(left,right+1):
        arr[s]=temp[p]
        p+=1
    return count

def mergeSort(arr,left,right):
    count=0
    if right>left:
        mid=(left+right)//2
        countLeft=mergeSort(arr,left,mid)
        countRight=mergeSort(arr,mid+1,right)
        myCount=merge(arr,left,mid+1,right)
        return (myCount+countLeft+countRight)
    return count
def inversionCount(arr):
    print(mergeSort(arr,0,len(arr)-1))

n=int(input())
for i in range(n):
    p=int(input())
    l=list(map(int,input().split()))
    inversionCount(l)