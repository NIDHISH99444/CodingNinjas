## Read input as specified in the question.
## Print output as specified in the question.
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


n, edge = list(map(int, input().split()))
edges = [[0 for i in range(n)] for j in range(n)]
for i in range(edge):
    a, b = list(map(int, input().split()))
    addEdge(a, b)
visited = [False] * n
for i in range(n):
    if (visited[i] == False):
        bfs(edges, n, i)
