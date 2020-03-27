def stockSpan(arr):
    stack=[]
    newArr=[0]*len(arr)
    for i in range(len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            stack.pop()
        if not stack:
            newArr[i]=i
        else:
            newArr[i]=i-stack[-1]-1
        stack.append(i)
    return newArr

print(stockSpan([100,30,10,20,25,40,26,35,45]))
print(stockSpan([5,10,7,25,40]))