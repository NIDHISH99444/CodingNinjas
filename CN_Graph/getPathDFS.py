# def  bfs(edges,n,sv,ev,mp):
#     visited=[False]*n
#     pendingVertices=[]
#     pendingVertices.append(sv)
#     visited[sv]=True
#     while len(pendingVertices)!=0:
#         currVertices=pendingVertices.pop(0)
#         for i in range(n):
#             if i==currVertices:
#                 continue
#             if edges[currVertices][i]==1 and visited[i]==False:
#                 pendingVertices.append(i)
#                 visited[i]=True
#                 mp[i]=currVertices
def dfs(edge,n,visited,sv,end,mp):
    visited[sv]=True
    for i in range(n):
        if i ==sv:
            continue
        elif edges[sv][i]==1:
            if visited[i]==True:
                continue
            else:
                mp[i]=sv
                dfs(edges,n,visited,i,end,mp)

def addEdge(u,v):
    edges[u][v]=1
    edges[v][u]=1


n,edge=list(map(int,input().split()))
edges=[[0 for i in range(n)]for j in range(n)]
for i in range(edge):
    a,b=list(map(int,input().split()))
    addEdge(a,b)
# addEdge(0,1)
# addEdge(0,3)
# addEdge(1,2)
# addEdge(2,3)
visited=[False]*n
mp={}
start,end=list(map(int,input().split()))
dfs(edges,n,visited,start,end,mp)


if mp!={}:
    print(end,end=" ")
    while end!=start:
         print(mp[end],end=" ")
         end=mp[end]

