def powerOfNumner(x,n):
    if n==0:
        return 1
    return x*powerOfNumner(x,n-1)

print(powerOfNumner(3,0))
