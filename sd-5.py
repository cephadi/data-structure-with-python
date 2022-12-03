# implementasi graph
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = []
        self.graph = graph_dict
    
    def get_vertices(self):
        # get simpul/sudut
        return list(self.graph.keys())

    def edges(self):
        return self.find_edges()
    
    def find_edges(self):
        edges_name = []
        for vrtx in self.graph:
            for nxvrtx in self.graph[vrtx]:
                if {nxvrtx, vrtx} not in edges_name:
                    edges_name.append({vrtx, nxvrtx})
        return edges_name
    
    def insert_vertices(self, key_vrtx):
        if key_vrtx not in self.graph:
            self.graph[key_vrtx] = []
    
    def insert_edges(self, new_edge):
        # {'a', 'c'}
        new_edge = set(new_edge)
        (vrtx1, vrtx2) = tuple(new_edge)
        if vrtx1 in self.graph:
            self.graph[vrtx1].append(vrtx2)
        else:
            self.graph[vrtx1] = [vrtx2]

graph_element = {
    "a" : ["b", "c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["b", "c", "e"],
    "e" : ["d"],
}

graph = Graph(graph_element)
print("== list simpul/sudut ==")
print(graph.get_vertices())
print("== after insert simpul/sudut ==")
graph.insert_vertices("f")
print(graph.get_vertices())
print("== list tepi an ==")
print(graph.edges())
print("== after insert tepi an ==")
graph.insert_edges({'a', 'c'})
graph.insert_edges({'a', 'e'})
graph.insert_edges({'b', 'e'})
print(graph.edges())
