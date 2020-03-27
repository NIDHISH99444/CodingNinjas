def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1
def dfsUtil(edge,n,visited,sv,res):
    res.append(sv)
    visited[sv]=True
    for i in range(n):
        if i ==sv: 
            continue
        elif edges[sv][i]==1:
            if visited[i]==True:
                continue
            else:
                dfsUtil(edges,n,visited,i,res)

def dfs(edge,n):
    for i in range(n):
        visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            res=[]
            dfsUtil(edge,n,visited,i,res)
            res.sort()
            for ele in res:
                print(ele,end=" ")
            print()
            res=[]


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
