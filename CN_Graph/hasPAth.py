def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1
def dfs(edge,n,visited,sv,ev):
    if edges[sv][ev]==1:
        visited[ev]==True
        return True
    visited[sv]=True
    for i in range(n):
        if i ==sv:
            continue
        elif edges[sv][i]==1:
            if visited[i]==True:
                continue
            else:
                dfs(edges,n,visited,i,ev)

n,m=list(map(int,input().split()))
edges=[[0 for i in range(n)]for j in range(n)]
visited=[False]*n
for i in range(m):
    a,b=list(map(int,input().split()))
    addEdge(a,b)
startEdge,endEdge=list(map(int,input().split()))

val=dfs(edges,n,visited,startEdge,endEdge)
if val==True:
    print("true")
else:
    print("false")
