'''
Question: Implement a graph using an adjacency list and write a function to add an edge between two vertices.
'''

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

# Test the Graph class
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
print(graph.adj_list)  # Output: {0: [1, 2], 1: [0], 2: [0]}
