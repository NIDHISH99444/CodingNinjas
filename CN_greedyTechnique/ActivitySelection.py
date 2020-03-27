def activitySelection(intervals):
    intervals=sorted(intervals,key=lambda x:x[1])
    endTime,cnt=0,0
    resArray=[]
    for i in range(len(intervals)):
        if intervals[i][0]>=endTime:
            resArray.append(intervals[i])
            endTime=intervals[i][1]
            cnt+=1

    return  cnt



n=int(input())
intervals=[]
for i in range(n):
    intervals.append(list(map(int,input().split())))

print(activitySelection(intervals))