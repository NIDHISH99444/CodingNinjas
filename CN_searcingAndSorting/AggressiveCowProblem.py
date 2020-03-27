def check(position,distance,cows):
    count=1
    last_index=position[0]
    for i in range(1,len(position)):
        if position[i]-distance>=last_index:
            last_index=position[i]
            count+=1
        if count==cows:
            return True
    return False
def aggressiveCowProblem(position,cows):
    position.sort()
    start=0
    end=position[len(position)-1]-position[0]
    ans=-1
    while start<=end:
        mid =start+(end-start)//2
        if check(position,mid,cows):
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans
#
n=int(input())
res=[]
ipt,cows=map(int,input().split())
print(ipt,cows)
for i in range(ipt):
    res.append(int(input()))
print(aggressiveCowProblem(res,cows))

#print(aggressiveCowProblem([100000000,500000000,900000000,1],2))
#
# 1
# 20 3
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
#
# 1
# 4 2
# 100000000
# 500000000
# 900000000
# 1