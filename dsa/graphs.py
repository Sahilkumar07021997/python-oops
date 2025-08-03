from collections import defaultdict


class DirectedGraph:
    """A class to represent a directed graph using an adjacency list."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = defaultdict(list)

    def insert_edge(self, v1, v2):
        """Insert an edge between two vertices in the graph."""
        self.graph[v1].append(v2)
        # 1 => 2, 3 means 1: [2, 3]

    def print_graph(self):
        """Print the graph in a readable format."""
        for vertex, edges in self.graph.items():
            print(f"{vertex} => {', '.join(map(str, edges))}")


g = DirectedGraph()
# Example usage of the Graph class and create a cyclic graph.
g.insert_edge(1, 2)
g.insert_edge(1, 100)
g.insert_edge(2, 3)
g.insert_edge(3, 4)
g.insert_edge(4, 1)

g.print_graph()
print("------------Directed graph created end.---------")


class UndirectedGraph:
    """A class to represent an undirected graph using an adjacency list."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = defaultdict(set)

    def insert_edge(self, v1, v2):
        """Insert an edge between two vertices in the graph."""
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)  # Add the reverse edge for undirected graph

    def print_graph(self):
        """Print the graph in a readable format."""
        for vertex, edges in self.graph.items():
            print(f"{vertex} => {', '.join(map(str, edges))}")


g_undirected = UndirectedGraph()
# Example usage of the UndirectedGraph class.
g_undirected.insert_edge(1, 2)
g_undirected.insert_edge(1, 100)
g_undirected.insert_edge(2, 3)
g_undirected.insert_edge(3, 4)

g_undirected.print_graph()
