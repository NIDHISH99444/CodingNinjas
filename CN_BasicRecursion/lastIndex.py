def lastIndex(arr,x,count=0):
    if len(arr)==0:
        return -1

    index=lastIndex(arr[1:],x,count+1)
    if index==-1 and arr[0]==x:
        return count
    else:
        return index

print(lastIndex([8,9,10,9],10))