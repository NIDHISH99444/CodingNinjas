def intervalScheduling(intervals):
    intervals=sorted(intervals,key=lambda x:x[1])
    res=[]
    ep=0
    for i in range(len(intervals)):
        if intervals[i][0]>ep:
            ep=intervals[i][1]
            res.append(intervals[i])
    return res
  


interval=[[5, 9],[1, 2], [3, 4], [0, 6], [5, 7],[8, 9]]


print(intervalScheduling(interval))