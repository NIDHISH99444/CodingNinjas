def sumUpTo(val):
    sum=0
    while val:
        sum+=val%10
        val=val//10
    return sum


n=int(input())
for i in range(n):
    print(sumUpTo(int(input())))