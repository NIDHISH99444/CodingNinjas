def mergeOverlappingIntervals(intervals):

    intervals=sorted(intervals,key=lambda x:x[0])

    res=[intervals[0]]
    for i in range(1,len(intervals)):
        if res[-1][1]<intervals[i][0]:
            res.append(intervals[i])
        else:
            res[-1][1]=max(intervals[i][1],res[-1][1])
    print(res)

#print(mergeOverlappingIntervals([[1, 3], [2, 5], [6, 8], [9, 14], [13, 20], [100, 120]]))
mergeOverlappingIntervals([[6,8],[2,5],[1,3],[13,20],[9,14],[100,120]])