def pow(x,n):
    if n<0:
        return 1/helper(x,-n)
    else:
        return helper(x,n)

def helper(x,n):
    if x==0:
        return 0
    if n==0:
        return 1
    if n%2==0:
        return helper(x*x,n//2)
    else:
        return x*helper(x*x,n//2)