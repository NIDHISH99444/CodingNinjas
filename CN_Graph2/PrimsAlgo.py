import  sys
def getMinVertex(weight,visited,n):
    minVertex=-1
    for i in range(n):
        if visited[i]==False and (minVertex==-1 or weight[minVertex]>weight[i]):
            minVertex=i
    return minVertex
def prims(edges,n):
    visited=[False]*n
    parent=[-1]*n
    weight=[sys.maxsize]*n
    weight[0]=0
    for i in range(0,n-1):
        #get minVertex from unvisited vertices
        minVertex=getMinVertex(weight,visited,n)
        visited[minVertex]=True
        #explore all the neighbour of minVertex and update parent and weight according to that
        for j in range(n):
            if edge[minVertex][j]!=0 and visited[j]==False:
                if weight[j]>edge[minVertex][j]:
                    weight[j]=edge[minVertex][j]
                    parent[j]=minVertex

    for i in range(1,n):
        if parent[i]<i:
            print(parent[i],i,weight[i])
        else:
            print(i,parent[i],weight[i])

interval=[]
n,m=list(map(int,input().split()))
edge=[[0 for i in range(n)]for j in range(n)]
for i in range(m):
    lst=list(map(int,input().split()))
    interval.append(lst)

for i in range(len(interval)):
    edge[interval[i][0]][interval[i][1]]=interval[i][2]
    edge[interval[i][1]][interval[i][0]] = interval[i][2]

prims(edge,n)