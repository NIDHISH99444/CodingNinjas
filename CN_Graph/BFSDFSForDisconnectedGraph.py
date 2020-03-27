def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1
def dfsUtil(edge,n,visited,sv):
    print(sv,end=" ")
    visited[sv]=True
    for i in range(n):
        if i ==sv:
            continue
        elif edges[sv][i]==1:
            if visited[i]==True:
                continue
            else:
                dfsUtil(edges,n,visited,i)



def dfs(edge,n):
    for i in range(n):
        visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            dfsUtil(edge,n,visited,i)

def  bfsUtil(edges,n,sv,visited):
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

def bfs(edge,n):
    for i in range(n):
        visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            bfsUtil(edge,n,i,visited)


n=7
edges=[[0 for i in range(n)]for j in range(n)]
visited=[False]*n

addEdge(0, 2)
addEdge(0, 3)
addEdge(2,3)
addEdge(1, 4)
addEdge(5,6)

print("DFS for disconnected components")
dfs(edges,n)
print()
print("BFS for disconnected components")
bfs(edges,n)