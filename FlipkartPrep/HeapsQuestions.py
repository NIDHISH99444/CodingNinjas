import heapq
from heapq import heappop,heappush,heappushpop
res=[]
def sortKsorted(arr,k):
    heap=[]
    for i in range(len(arr)):
        heapq.heappush(heap,arr[i])
        if len(heap)>k:
            res.append(heapq.heappop(heap))
    while heap:
        res.append(heapq.heappop(heap))
    return res



arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
arr=[10, 9, 8, 7, 4, 70, 60, 50]
k=4

#print(sortKsorted(arr,k))


def findClosestElements( arr, k, x) :

    k_closest = []
    for num in arr:
        if len(k_closest) == k:
            heappush(k_closest, (-abs(x - num), -num))
            heappop(k_closest)
        else:
            heappush(k_closest, (-abs(x - num), -num))
    return sorted([-tup[1] for tup in k_closest])

#print(findClosestElements([1,2,3,4,5],4,3))

def topKfreq(arr,k):
    topk=[]
    dict={}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    for ele in dict:
        heapq.heappush(topk,(dict[ele],ele))
        if len(topk)>k:
            heapq.heappop(topk)
    return sorted([ele[1] for ele in topk])


#print(topKfreq([1,1,1,2,2,3,4],2))

def kclosestOrigin(arr,k):
    closest=[]
    for i in range(len(arr)):

        heapq.heappush(closest,(-(arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1]),arr[i][0],arr[i][1]))
        if len(closest)>k:
            heapq.heappop(closest)

    while closest:
        dist,x,y=heapq.heappop(closest)
        print(x,y)

arr=[[1,3],[-2,2],[5,8],[0,1]]
k=2
#kclosestOrigin(arr,k)

def maxCost(arr):
    cost=0
    rodWindow=[]
    for i in range(len(arr)):
        heapq.heappush(rodWindow,arr[i])
    while len(rodWindow)>=2:
        first=heapq.heappop(rodWindow)
        sec=heapq.heappop(rodWindow)
        cost+=first+sec
        heapq.heappush(rodWindow,first+sec)
    return cost
print(maxCost([1,2,3,4,5]))