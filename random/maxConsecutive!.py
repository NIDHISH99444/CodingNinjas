def maxCons(arr,k):
    i,j=0,0
    res=0
    while i<len(arr):
        if arr[i]==0:
            k-=1
        if k==0:
            res=max(res,i-j+1)
        if k<0:
            if arr[j]==0:
                k+=1
            j+=1
        i+=1
    return res


print(maxCons([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
