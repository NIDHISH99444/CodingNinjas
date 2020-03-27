def winningLottery(sum,digit):
    arr=[0]*digit
    arr[0]=1
    finalSum=sum-1
    for i in range(digit-1,0,-1):
        if finalSum>=9:
            arr[i]=9
            finalSum-=9
        else:
            arr[i]=finalSum
            finalSum=0
    if finalSum>0:
        arr[0]+=finalSum
    finalNumber=0
    for i in range(len(arr)):
        finalNumber=finalNumber*10+arr[i]
    print(finalNumber)


sum,digit=list(map(int,input().split()))
winningLottery(sum,digit)