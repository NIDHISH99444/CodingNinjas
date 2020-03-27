def closestElementGreaterOnRight(arr):
    newArray=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        if stack and arr[i]>arr[stack[-1]]:
            while stack and arr[i]>arr[stack[-1]]:
                newArray[stack[-1]]=arr[i]
                stack.pop()
        stack.append(i)
    print(newArray)


closestElementGreaterOnRight([10,20,1,5,25,500,60])