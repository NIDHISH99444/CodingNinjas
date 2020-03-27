def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1
def dfs(edge,n,visited,sv):
    print(sv,end=" ")
    visited[sv]=True
    for i in range(n):
        if i ==sv:
            continue
        elif edges[sv][i]==1:
            if visited[i]==True:
                continue
            else:
                dfs(edges,n,visited,i)




n=4
edges=[[0 for i in range(n)]for j in range(n)]
visited=[False]*n

addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 2)
addEdge(2, 0)
addEdge(2, 3)
addEdge(3, 3)
print(edges)
dfs(edges,n,visited,0) 
