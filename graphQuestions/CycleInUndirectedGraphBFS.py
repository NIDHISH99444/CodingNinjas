from collections import defaultdict


def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)


def isConnected(i,V,visited):
    parent=[-1]*V
    queue=[]
    queue.append(i)
    visited[i]=True
    while queue:
        u=queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v]=True
                queue.append(v)
                parent[v]=u
            elif parent[u]!=v:
                return True
    return False

def isCyclicDisconnected(graph,V):
    visited=[False]*V
    for i in range(V):
        if not visited[i] and isConnected(i,V,visited):
            return True
    return False

if __name__ == "__main__":
    V = 4
    graph=[]
    graph = [[] for i in range(V)]

    addEdge(graph, 0, 1)
    addEdge(graph, 1, 2)
    addEdge(graph, 2, 0)
    addEdge(graph, 2, 3)

    if isCyclicDisconnected(graph, V):
        print("Yes")
    else:
        print("No")