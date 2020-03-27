def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1

def rotateArray(arr,d):
    if d==0 :
        return
    reverse(arr,0,d-1)
    reverse(arr,d,len(arr)-1)
    reverse(arr,0,len(arr)-1)


    for ele in arr:
        print(ele,end=" ")


n=int(input())
m=(list(map(int,input().split())))
d=int(input())
rotateArray(m,d)
