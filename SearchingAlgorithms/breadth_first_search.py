# Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. 
# It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key') and explores the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. 
# BFS is particularly useful for finding the shortest path on unweighted graphs.

from collections import deque

# class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = {}  # dictionary to store graph

    # function to add an edge to graph
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    # function to print a BFS of graph
    def BFS(self, s):
        # mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # queue for BFS
        queue = deque()

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # dequeue a vertex from queue and print it
            s = queue.popleft()
            print(s, end=" ")

            # get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# graph 
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)
