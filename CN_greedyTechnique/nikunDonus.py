def nikunjDonuts(arr):
    arr.sort(reverse=True)
    res=0
    for i in range(len(arr)):
        res+=arr[i]*pow(2,i)
    return  res



n=int(input())
arr=list(map(int,input().split()))
print(nikunjDonuts(arr))