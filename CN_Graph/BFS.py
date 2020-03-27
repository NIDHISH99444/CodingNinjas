def  bfs(edges,n,sv):
    visited=[False]*n
    pendingVertices=[]
    pendingVertices.append(sv)
    visited[sv]=True
    while len(pendingVertices)!=0:
        currVertices=pendingVertices.pop(0)
        print(currVertices,end=" ")
        for i in range(n):
            if i==currVertices:
                continue
            if edges[currVertices][i]==1 and visited[i]==False:
                pendingVertices.append(i)
                visited[i]=True
    return visited
def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1


n,edge=list(map(int,input().split()))
edges=[[0 for i in range(n)]for j in range(n)]
for i in range(edge):
    a,b=list(map(int,input().split()))
    addEdge(a,b)
for i in range(n):
    if(visited[i]==False):
        bfs(edges,n,i)
bfs(edges,n,0)