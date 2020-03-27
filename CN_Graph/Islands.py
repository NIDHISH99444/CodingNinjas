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
    cnt=0
    for i in range(n):
        if visited[i]==False:
            res=[]
            dfsUtil(edge,n,visited,i,res)
            cnt+=1
    return cnt

n,m=list(map(int,input().split()))
edges=[[0 for i in range(n)]for j in range(n)]
visited=[False]*n

u=list(map(int,input().split()))
v=list(map(int,input().split()))
for i in range(m):
    addEdge(u[i]-1,v[i]-1)


print(dfs(edges,n))
