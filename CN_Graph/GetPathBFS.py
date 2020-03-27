def  bfs(edges,n,sv,ev,mp):
    visited=[False]*n
    pendingVertices=[]
    pendingVertices.append(sv)
    visited[sv]=True
    while len(pendingVertices)!=0:
        currVertices=pendingVertices.pop(0)
        for i in range(n):
            if i==currVertices:
                continue
            if edges[currVertices][i]==1 and visited[i]==False:
                pendingVertices.append(i)
                visited[i]=True
                mp[i]=currVertices

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
mp={}
start,end=list(map(int,input().split()))
bfs(edges,n,start,end,mp)


def printPath(mp,start,end):
    flag=0
    for key,val in mp.items():
        if val==start:
            flag=1
            break
    if flag==1:
        print(end, end=" ")
        while end!=start:
            print(mp[end],end=" ")
            end=mp[end]



printPath(mp,start,end)
#     print(end,end=" ")
#     while end!=start:
#          print(mp[end],end=" ")
#          end=mp[end]

