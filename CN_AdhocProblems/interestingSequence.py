import  sys
def interestingSequence(arr,costID,costI):
    minVal=min(arr)
    maxVal=max(arr)
    finalCost=sys.maxsize
    for j in range(minVal,maxVal+1):
        pivot,inc,dec,cost=j,0,0,0
        for i in range(len(arr)):
            if arr[i]>pivot:
                dec+=(arr[i]-pivot)
            elif arr[i]<pivot:
                inc+=(pivot-arr[i])
        if inc>=dec:
            cost=dec*costID+(inc-dec)*costI
            finalCost=min(cost,finalCost)

    return finalCost

n,incDecCost,incCost=list(map(int,input().split()))

lst=[int(i) for i in input().split()]
print(interestingSequence(lst,incDecCost,incCost))
