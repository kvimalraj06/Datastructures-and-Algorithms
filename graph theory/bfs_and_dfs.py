class Graph():
    def __init__(self):
        self.graph_dict={}
    def vertices(self):
        self.vertics=[]
        for i in self.graph_dict.keys():
            self.vertics.append(i)
        return(" ".join(list(map(str,self.vertics))))
    def edges(self):
        self.edge = []
        for vertex in self.graph_dict:
            for edges in self.graph_dict[vertex]:
                self.edge.append((vertex, edges))
        return (self.edge)
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
    def add_edges(self,vertex1,vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            l=[]
            l.append(vertex2)
            self.graph_dict[vertex1] = l
    def bfs(self,s):
        visited = {}
        for i in self.graph_dict:
            visited[i] = False
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph_dict[s]:
                if visited[i] == False :
                    queue.append(i)
                    visited[i]=True
    def print_graph(self):
        return self.graph_dict
    def dfsutil(self,v,visited):
        visited[v] = True
        print(v, end=" ")
        for i in self.graph_dict[v]:
            if visited[i]==False:
                self.dfsutil(i,visited)
    def dfs(self,v):
        visited={}
        for i in self.graph_dict:
            visited[i]=False
        self.dfsutil(v,visited)

g = Graph()
g.add_edges("a", "b")
g.add_edges("a", "c")
g.add_edges("a", "e")
g.add_edges("b", "a")
g.add_edges("b", "d")
g.add_edges("b", "e")
g.add_edges("c", "a")
g.add_edges("c", "f")
g.add_edges("c", "g")
g.add_edges("e", "a")
g.add_edges("d", "b")
g.add_edges("e", "b")
g.add_edges("f", "c")
g.add_edges("g", "c")
print(g.print_graph())
print("Following is Breadth First Traversal"
      " (starting from vertex a)")
g.bfs("a")
print()
print("Following is Depth First Traversal"
      " (starting from vertex a)")
g.dfs("a")