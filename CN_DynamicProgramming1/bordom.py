def boredom(arr):
    freq,dp=[0]*12,[0]*11
    for i in range(len(arr)):
        freq[arr[i]]+=1

    dp[0]=0
    dp[1]=freq[1]
    for i in range(2,11):
        dp[i]=max(dp[i-1],dp[i-2]+i*freq[i])
    print(dp)
    return dp[10]


#arr=[1,2,3,4,2,4,1,5,5]
#n=int(input())
#arr=list(map(int,input().split()))
print(boredom([1,2,10,10,9,9,9]))