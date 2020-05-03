# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), check if there exists any path between them or not. Print true or false.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
# Line (E+2) : Two integers v1 and v2 (separated by space)
# Output Format :
# true or false
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# 0 <= v1, v2 <= V-1
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# true
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :
# false

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
