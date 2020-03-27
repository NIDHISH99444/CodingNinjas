def addEdge(u,v):
    edges[u-1][v-1]=1
    edges[v-1][u-1]=1

def dfs(edge,n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            elif edges[i][j]==1:
                for k in range(n):
                    if i==k or j==k :
                        continue
                    elif edge[j][k]==1 and edges[k][i]==1:
                        count[0]+=1
    return count[0]




count=[0]


n,m=list(map(int,input().split()))
edges=[[0 for i in range(n)]for j in range(n)]
u=list(map(int,input().split()))
v=list(map(int,input().split()))
for i in range(m):
    addEdge(u[i],v[i])






dfs(edges,n)
print(count[0]//6)