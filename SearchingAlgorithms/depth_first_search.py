# Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
# The algorithm starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking. 
# This makes DFS particularly useful for tasks like checking connectivity and finding paths in a maze or puzzle, exploring all possible solutions before retreating to earlier states.

# class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    # add an edge to graph
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    # function used by DFS
    def DFS_util(self, v, visited):
        # mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')

        # recur for all the vertices adjacent to this vertex
        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.DFS_util(neighbour, visited)

    # function to do DFS traversal. It uses recursive DFS_util()
    def DFS(self, v):
        # a set to store visited vertices
        visited = set()

        # crecursive helper function to print DFS traversal
        self.DFS_util(v, visited)

# graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is DFS starting from vertex 2")
g.DFS(2)
