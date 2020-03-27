import bisect
def chefProblem(interval,val):
    interval=sorted(interval,key=lambda x :  x[0])
    n=len(interval)
    if val>interval[-1][1]:
        print("-1")
        return
    position=bisect.bisect_left(interval,(val,))
    print(interval[position])
    print(position)
    if position==0:
        ans=interval[position][0]-val
        print(ans)
    else:
        ans=-1
        if interval[position-1][1]>val:
            ans=0
        else:
            ans=interval[position][0]-val
    print(ans)


chefProblem([(3,4),(4,5),(7,9),(20,23)],10)