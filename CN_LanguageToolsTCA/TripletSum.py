def TripletSum(arr,sum):
    arr.sort()

    for i in range(len(arr)-2):
        val=sum-arr[i]
        j=i+1
        k=len(arr)-1
        while j<k:
            if arr[j]+arr[k]>val:
                k-=1
            elif arr[j]+arr[k]<val:
                j+=1
            else:
                leftCounter=0
                rightCounter=0
                for ptr in range(j,k+1):
                    if arr[ptr]==arr[j]:
                        leftCounter+=1
                    else:
                        break
                for ptr in range(k,j-1,-1):
                    if arr[ptr]==arr[k]:
                        rightCounter+=1
                    else:
                        break
                total=leftCounter*rightCounter
                if arr[j]==arr[k]:
                    total=((k-j+1)*(k-j))//2
                for s in range(total):
                    print(arr[i],arr[j],arr[k])
                j+=leftCounter
                k-=rightCounter

TripletSum([1,2,3,3,3,4,4,4],7)



#70
#9 5 7 27 22 21 2 7 10 12 3 26 10 19 18 24 9 30 12 18 12 13 11 18 3 3 12 22 29 19 11 21 29 3 1 9 5 26 29 23 30 27 8 11 12 20 5 28 5 3 11 22 18 24 12 29 25 17 29 18 20 18 25 27 10 5 30 29 5 14
#66