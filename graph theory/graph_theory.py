class Graph():
    def __init__(self, graph_dict):
        if graph_dict==None:
            self.graph_dict={}
        self.graph_dict=graph_dict
    def vertices(self):
        self.vertics=[]
        for i in self.graph_dict.keys():
            self.vertics.append(i)
        return(" ".join(list(map(str,self.vertics))))
    def edges(self):
        self.edge=[]
        for vertex in self.graph_dict:
            for edges in self.graph_dict[vertex]:
                self.edge.append((vertex, edges))
        return(self.edge)
    def add_vertex(self,vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex]=[]
    def add_edges(self,vertex1,vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            l=[]
            l.append(vertex2)
            self.graph_dict[vertex1] = l
    def print_graph(self):
        return self.graph_dict
if __name__ == "__main__":
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         1: ["a"]
         }
    graph = Graph(g)
    print(graph.vertices())
    print(graph.edges())
    graph.add_vertex('z')
    print(graph.vertices())
    graph.add_edges("z", "i")
    print(graph.edges())
    graph.add_edges('a', "k")
    graph.add_edges('a', "l")
    print(graph.print_graph())




