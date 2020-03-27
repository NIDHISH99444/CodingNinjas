def stairCase(n,memo):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    if memo[n]!=-1:
        return memo[n]
    res=stairCase(n-1,memo)+stairCase(n-2,memo)+stairCase(n-3,memo)
    memo[n]=res
    return memo[n]
n=6
memo=[-1]*(n+1)
print(stairCase(n,memo))

