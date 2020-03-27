def sumMeUp(arr):
    hs={}
    for i in range(len(arr)):
       if arr[i] not in hs:
           hs[arr[i]]=1
       else:
           hs[arr[i]]+=1
    print(hs)

    for i in range(len(arr)):
        if arr[i] in hs and -arr[i] in hs:
            sum =hs[arr[i]]*hs[-arr[i]]
            del hs[arr[i]]
            del hs[-arr[i]]
            for j in range(sum):
                minVal=min(arr[i],-arr[i])
                maxVal=max(arr[i],-arr[i])
                print(minVal,maxVal)




sumMeUp([2 ,1 ,-2 ,2, 3])