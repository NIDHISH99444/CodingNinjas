def dfsUtil(edges,visited,n,i,res):
    visited[i]=True
    res.append(i)
    for j in range(n):
        if i==j:
            continue
        elif edges[i][j]==1:
            if visited[j]==True:
                continue
            else:
                dfsUtil(edges,visited,n,j,res)




def dfs(edges,n,finalList):
    visited=[False]*n

    for i in range(n):
        res=[]
        if visited[i]==False:
            dfsUtil(edges,visited,n,i,res)
            finalList.append(res)
            res=[]


def addEdge(x,y):
    edges[x][y]=1
    edges[y][x]=1

n=6
edges=[[0 for i in range(n)] for j in range(n)]

addEdge(0,1)
addEdge(0,3)
addEdge(1,2) 
addEdge(2,3)
addEdge(4,5)
finalList=[]
dfs(edges,n,finalList)
print(finalList)