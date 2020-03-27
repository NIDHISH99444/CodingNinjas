def collectingTheBalls(balls):
    low=1
    store=0
    high=balls
    while low<=high:
        mid=(low+high)//2
        if checkK(balls,mid):
            store=mid
            high=mid-1
        else:
            low=mid+1
    return store

def checkK(balls,mid):
    sum=0
    currBalls=balls
    while currBalls>0:
        sum+=min(mid,currBalls)
        currBalls-=mid
        currBalls=currBalls-(currBalls//10)
    if 2*sum>=balls:
        return True
    return False


n=int(input())
print(collectingTheBalls(n))

