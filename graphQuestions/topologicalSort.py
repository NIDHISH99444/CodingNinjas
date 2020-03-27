from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.vertices=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topology(self,i,visited,stack):
        visited[i]=True
        for e in self.graph[i]:
            if visited[e]==False:
                self.topology(e,visited,stack)
        stack.insert(0,i)

    def topologicalSort(self):
        stack=[]
        visited=[False]*self.vertices
        for i in range(self.vertices):
            if visited[i]==False:
                self.topology(i,visited,stack)
        print(stack)




g=Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

print("Following is a Topological Sort of the given graph")
g.topologicalSort()