def intervalScheduling(interval):
    interval=sorted(interval,key=lambda x:x[1])
    print(interval)
    end=0
    res=[]
    for i in range(0,len(interval)):
        if interval[i][0]>end:
            res.append(interval[i])
            end=interval[i][1]
    print(res)


intervalScheduling([[1, 2], [3, 4], [0, 6], [5, 7], [5, 9], [8, 9]])
#intervalScheduling([[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]])