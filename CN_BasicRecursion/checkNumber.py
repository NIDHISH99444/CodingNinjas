def checkNumber(arr,x):
    if len(arr)==0:
        return False
    if arr[0]==x:
        return True
    return checkNumber(arr[1:],x)

print(checkNumber([9,8,1],10))
