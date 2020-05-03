def nextGreatestElement(arr):
    stack=[]
    res=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            res.append(-1)
        if len(stack)>0 and arr[i]>=stack[-1]:
            while len(stack)>0 and arr[i]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
        elif len(stack)>0 and arr[i]<stack[-1]:
            res.append(stack[-1])
        stack.append(arr[i])
    return res[::-1]

print(nextGreatestElement([1,2,1]))


def nextGreaterElements( A):
    stack, res = [], [-1] * len(A)
    for i in range(len(A)*2) :
        while stack and (A[stack[-1]] < A[i]):
            res[stack.pop()] = A[i]
        stack.append(i)
    return res

print(nextGreaterElements([1,2,1]))