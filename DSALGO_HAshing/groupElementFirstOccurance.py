def groupElementByFirstOccurances(arr):
    hm={}
    for i in range(len(arr)):
        hm[arr[i]]=hm.get(arr[i],0)+1
    print(hm)

    for i in range(len(arr)):
        count=hm.get(arr[i],None)
        if count!=None:
            while count>0:
                print(arr[i],end=" ")
                count-=1
            del hm[arr[i]]

groupElementByFirstOccurances([5, 3, 5, 1, 3, 3])
