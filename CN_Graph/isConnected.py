# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# "true" or "false"
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
# Sample Input 2:
# 4 3
# 0 1
# 1 3
# 0 3
# Sample Output 2:
# false
# Sample Output 2 Explanation
# The graph is not connected, even though vertices 0,1 and 3 are connected to each other but there isn’t any path from vertices 0,1,3 to vertex 2.

def addEdge(u, v):
    edges[u][v] = 1
    edges[v][u] = 1


def dfs(edge, n, visited, sv):
    visited[sv] = True
    for i in range(n):
        if i == sv:
            continue
        elif edges[sv][i] == 1:
            if visited[i] == True:
                continue
            else:
                dfs(edges, n, visited, i)


n, edge = list(map(int, input().split()))
edges = [[0 for i in range(n)] for j in range(n)]
for i in range(edge):
    a, b = list(map(int, input().split()))
    addEdge(a, b)
visited = [False] * n
dfs(edges, n, visited, 0)


def checkConnected(visited):
    for i in range(n):
        if visited[i] == False:
            return 0
    return 1


check = checkConnected(visited)
if check:
    print("true")
else:
    print("false")


