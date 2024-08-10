<<<<<<< HEAD:competitive Programing-chatGpt/graph_represantation/graph_rep.py
<<<<<<< HEAD
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/graph_represantation/graph_rep.py
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
<<<<<<< HEAD:competitive Programing-chatGpt/graph_represantation/graph_rep.py
=======
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
>>>>>>> c4f5223ba10d71953b90e01d93359193ccea7503
=======
>>>>>>> b1e894c8f4f88706e4e6472a63308c77b347ce99:Competitive_programing/graph_represantation/graph_rep.py
