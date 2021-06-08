# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def dfs_util(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    # The function to do dfs traversal. It uses
    # recursive dfs_util()
    def dfs(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.dfs_util(v, visited)

# This code is contributed by Neelam Yadav
# Edited by Ethan Pitzer 2021-6-07
