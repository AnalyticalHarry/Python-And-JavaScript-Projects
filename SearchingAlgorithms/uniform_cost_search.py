# Uniform Cost Search (UCS), also known as Dijkstra's algorithm when used for finding the shortest path between nodes in a graph, 
# it is a searching algorithm that is used for traversing or searching a weighted graph. 
# The goal is to find the least cost path from a given starting node to a target node.
# UCS expands the least cost node first and guarantees to find the least cost path to the goal if the cost of each edge is non-negative.

# Importing the heapq module for implementing priority queue.
import heapq  

class Graph:
    def __init__(self):
      # empty dictionary to represent the graph.
        self.graph = {}  

    def add_edge(self, u, v, cost):
         # If starting node is not already in the graph.
        if u not in self.graph:  
           # add the starting node to the graph.
            self.graph[u] = [] 
           # append the ending node and its cost to the starting node's list of neighbors.
        self.graph[u].append((v, cost)) 

    def ucs(self, start, goal):
       # an empty set to keep track of visited nodes.
        visited = set() 
       # queue with a tuple containing the cost (0 for the starting node) and the starting node itself.
        priority_queue = [(0, start)] 
       # continue looping until the priority queue is empty.
        while priority_queue: 
            # pop the node with the least cost from the priority queue.
            (cost, current_vertex) = heapq.heappop(priority_queue)  
            # if the current node has already been visited.
            if current_vertex in visited:  
                continue
            # mark the current node as visited.
            visited.add(current_vertex)  
             # if the current node is the goal node.
            if current_vertex == goal: 
                print("Cost to reach {} is {}".format(goal, cost))  
               # return the cost to reach the goal.
                return cost 
             # iterate over the neighbors of the current node.
            for neighbor, weight in self.graph.get(current_vertex, []): 
              # if the neighbor has not been visited.
                if neighbor not in visited:  
                   # add the neighbor to the priority queue with updated cost.
                    heapq.heappush(priority_queue, (cost + weight, neighbor)) 
        # If there's no path from start to goal.
        return float("inf")  


g = Graph()  
# adding edges to the graph.
g.add_edge('A', 'B', 1) 
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 2)
 # Uniform Cost Search from node 'A' to node 'E'. Expected output: Cost to reach E is 5
g.ucs('A', 'E') 
