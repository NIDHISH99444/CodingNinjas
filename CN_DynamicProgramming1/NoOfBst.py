MOD=1000000007
def numberOfBST(n):
    if dp[n]>1:
        return dp[n]
    if n==0 or n==1 :
        return 1

    cnt=0
    for i in range(n):
        cnt = (cnt % MOD + (numberOfBST(i) % MOD * numberOfBST(n - i - 1) % MOD) % MOD) % MOD
    dp[n]=cnt
    return cnt

n=int(input())
dp=[1]*(n+1)
print(numberOfBST(n))