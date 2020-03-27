import  heapq
def connectnRopesWithMinimumCost(ropes):
    heap=[]
    for i in range(len(ropes)):
        heapq.heappush(heap,ropes[i])
    print(heap)
    while len(heap)>1:
        first=heapq.heappop(heap)
        second=heapq.heappop(heap)
        sum=first+second
        heapq.heappush(heap,sum)
    print(heap)

connectnRopesWithMinimumCost([2,3,5,7,9,13])