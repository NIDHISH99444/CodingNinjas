# Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
# Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# Different components in new line
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# Sample Input 1:
# 4 2
# 0 1
# 2 3
# Sample Output 1:
# 0 1
# 2 3
# Sample Input 2:
# 4 3
# 0 1
# 1 3
# 0 3
# Sample Output 2:
# 0 1 3
# 2
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
