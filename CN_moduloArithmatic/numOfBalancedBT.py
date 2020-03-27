MOD = 1000000007


def balancedBTBF(h):
    # base cases
    dp[0] = 1
    dp[1] = 1

    for i in range(2, h + 1):
        #dp[i] = (dp[i - 1] * ((2 * dp[i - 2]) % MOD + dp[i - 1]) % MOD) % MOD
        dp[i]=(((dp[i-1]*dp[i-1])%MOD+(2*dp[i-2]*dp[i-1])%MOD)%MOD)
    return dp[h]

def newBalanced(h):
    if h==1 or h==0 :
        return 1
    x=newBalanced(h-1)
    y=newBalanced(h-2)
    return (((x*x)%MOD+(2*x*y)%MOD)%MOD)

print(newBalanced(13))
from sys import setrecursionlimit

setrecursionlimit(11000)
h = int(input())
dp = [0 for i in range(h + 1)]
print(balancedBTBF(h))
