def merge(arr,left,mid,right):
    i=left
    j=mid
    k=0
    temp=[0]*(right-left+1)
    while i<mid and j<=right:
        if arr[i]<=arr[j]:
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k]=arr[j]
            k+=1
            j+=1
    while i<mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=arr[j]
        j+=1
        k+=1
    p=0
    for s in range(left,right+1):
        arr[s]=temp[p]
        p+=1

def mergeSort(arr,left,right):
    if left<right:
        mid=(left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        return merge(arr,left,mid+1,right)


arr=[12,11,13,5,6,7]
mergeSort(arr,0,len(arr)-1)
for ele in arr:
    print(ele,end=" ")
