import heapq
def findkthSmallest(matrix,k):
    arr,res=[],None
    heapq.heappush(arr,(matrix[0][0],0,0))
    while k>0:
        res,i,j=heapq.heappop(arr)
        if i==0 and j<len(matrix[0])-1:
            heapq.heappush(arr,(matrix[i][j+1],i,j+1))
        if i<len(matrix)-1:
            heapq.heappush(arr, (matrix[i+1][j], i+1, j))
        k-=1
    return res


matrix=[
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
print(findkthSmallest(matrix,3))