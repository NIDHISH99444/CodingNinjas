def targetMarbles(arr,k):
    hs={}
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum-k in hs:
            return [i,hs[sum-k]]
        hs[sum]=i



print(targetMarbles([9,1,2,3,4,5,5,16,17,19],10))