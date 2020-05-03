#
# Given an undirected and connected graph G(V, E), print its BFS traversal.
# Here you need to consider that you need to print BFS path starting from vertex 0 only.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Note : 1. Take graph input in the adjacency matrix.
# 2. Handle for Disconnected Graphs as well
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# BFS Traversal (separated by space)
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
# 0 1 3 2

#Note : BFS is always used when you want to know the fastest way to reach a node
def bfs(edges, n, sv):
    pendingVertices = []
    pendingVertices.append(sv)
    visited[sv] = True
    while len(pendingVertices) != 0:
        currVertices = pendingVertices.pop(0)
        print(currVertices, end=" ")
        for i in range(n):
            if i == currVertices:
                continue
            if edges[currVertices][i] == 1 and visited[i] == False:
                pendingVertices.append(i)
                visited[i] = True


def addEdge(u, v):
    edges[u][v] = 1
    edges[v][u] = 1

n=4
#n, edge = list(map(int, input().split()))
edges = [[0 for i in range(n)] for j in range(n)]
# for i in range(edge):
#     a, b = list(map(int, input().split()))
#     addEdge(a, b)
addEdge(0,1)
addEdge(0,3)
addEdge(1,2)
addEdge(2,3)
print(edges)
visited = [False] * n
for i in range(n):
    if (visited[i] == False):
        bfs(edges, n, i)
