from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, res):
        visited[v] = True
        res.append(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs(i, visited,res)

    def dfsFun(self,v):
        visited=[False] * (len(self.graph)+5)
        res=[]
        for node in range(2,7):
            if visited[node]==False:
                self.dfs(node,visited,res)
        print(res)


links=[[1,2],[1,3],[2,4],[3,4],[3,6],[6,7],[4,5]]

def newListForm(links):
    hs=[]
    for i in range(1,8):
        newList=[]
        for j in range(len(links)):
            if links[j][0]!=i and links[j][1]!=i:
                newList.append(links[j])
        hs.append(newList)
    return hs
newList=newListForm(links)
print(newList[0])
g = Graph()
for i in range(len(newList[0])):
#     u,v=newList[0][0][0],newList[0][0][1]
#     print(u,v)
    print(newList[0][i][0], newList[0][i][1])
    g.edge(newList[0][i][0], newList[0][i][1])


g.dfsFun(newList[0][0][0])

