
def dfs(graph,i,j):
    if i<0 or i>=len(graph) or j<0 or j>=len(graph[0]) or graph[i][j]==0:
        return
    if graph[i][j]==1:
        graph[i][j]=0
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    for s in range(len(rowNbr)):
        dfs(graph,i+rowNbr[s],j+colNbr[s])

def noOfIslands(graph):
    cnt=0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==1:
                dfs(graph,i,j)
                cnt+=1
    return cnt
graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

print(noOfIslands(graph))