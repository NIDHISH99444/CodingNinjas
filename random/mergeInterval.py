def merge(interval,new_interval):
    interval.append(new_interval)
    if len(interval)==0:
        return
    interval=sorted(interval,key=lambda x:x[0])
    print(interval)
    res=[interval[0]]


    for i in range(1,len(interval)):
        if interval[i][0]<res[-1][1]:
            res[-1][1]=max(res[-1][1],interval[i][1])
        else:
            res.append(interval[i])
    return res



interval=[[1,3],[0,2],[6,9]]
new_interval=[2,5]
print(merge(interval,new_interval))