def search(interval,limit,start,end):
    if start>end:
        return -1
    if start==end:
        if interval[start][1]<=limit:
            return start
        else:
            return -1
    mid=(start+end)//2
    if interval[mid][1]<=limit:
        answer=search(interval,limit,mid+1,end)
        if answer==-1:
            return mid
        else:
            return answer
    else:
        return search(interval,limit,start,mid-1)


def weightedJobScheduling(interval):
    interval=sorted(interval,key=lambda x:x[1])
    print(interval)
    dp=[0]*len(interval)

    dp[0]=interval[0][2]

    for i in range(1,len(interval)):
        including=interval[i][2]
        nonConflicting=-1
        # for j in range(i-1,-1,-1):
        #     if interval[j][1]<=interval[i][0]:
        #         nonConflicting=j
        #         break
        nonConflicting=search(interval,interval[i][0],0,i-1)
        if nonConflicting!=-1:
            including+=dp[nonConflicting]
        dp[i]=max(including,dp[i-1])

    print(dp)
    return dp[-1]





# n=int(input())
# interval=[]
# for i in range(n):
#     interval.append(list(map(int,input().split())))
#
# print(interval)
# print(weightedJobScheduling(interval))
#print(weightedJobScheduling([[3, 10, 100], [1, 2, 50], [6, 19, 100], [2, 100, 200]]))

print(weightedJobScheduling([[34, 58, 24], [17, 66, 35], [57, 81, 50], [8, 101, 87], [26, 105, 82], [39, 110, 72], [46, 140, 14], [87, 193, 97]]))