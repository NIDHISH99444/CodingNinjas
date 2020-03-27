def middle(arr,start,end,search):
    if end<start:
        return -1
    if start>=len(arr):
        return -1
    if start==end:
        if arr[start]==search:
            return start
        else:
            return -1
    mid=(start+end)//2
    if arr[mid]==search:
        return mid
    elif arr[mid]<search:
        return middle(arr,mid+1,end,search)
    else:
        return middle(arr,start,mid-1,search)

arr=[1,3,4,6,8,10]
#print(middle(arr,0,len(arr),-1))
#print(middle(arr,0,len(arr),5))
#print(middle(arr,0,len(arr),2))
#print(middle(arr,0,len(arr),9))
print(middle(arr,0,len(arr),11))



