def rearrange(arr):
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]+1:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

def checkArraySorted(arr):
    if len(arr)==1:
        return True
    if arr[0]<arr[1]:
        return checkArraySorted(arr[1:])
    return False

#arr=[1,0,3,2]
# arr=[3,2,1]
n=int(input())
for i in range(n):
    noOfEmployee=int(input())
    EmployeeArray=list(map(int,input().split()))
    newArray=rearrange(EmployeeArray)
    #print(newArray)
    if checkArraySorted(newArray):
        print("Yes")
    else:
        print("No")

