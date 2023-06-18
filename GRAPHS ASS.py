#!/usr/bin/env python
# coding: utf-8

# # Breadth First Traversal for a Graph:

# In[1]:


from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_first_traversal(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth First Traversal (starting from vertex 2):")
g.breadth_first_traversal(2)


# # Depth First Traversal for a Graph:

# In[2]:


from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def depth_first_traversal(self, start_vertex):
        visited = set()

        def dfs(vertex):
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2):")
g.depth_first_traversal(2)


# # Count the number of nodes at a given level in a tree using BFS:

# In[4]:


from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_nodes_at_level(self, start_vertex, level):
        visited = set()
        queue = deque([(start_vertex, 0)])
        visited.add(start_vertex)
        count = 0

        while queue:
            vertex, curr_level = queue.popleft()

            if curr_level == level:
                count += 1

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, curr_level + 1))
                    visited.add(neighbor)

        return count


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)


# # Count the number of trees in a forest:

# In[6]:


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_trees_in_forest(self):
        visited = [False] * self.vertices
        count = 0

        def dfs(node):
            visited[node] = True

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for v in range(self.vertices):
            if not visited[v]:
                dfs(v)
                count += 1

        return count


g = Graph(5)  
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(3, 4)

print("Number of trees in the forest:", g.count_trees_in_forest())


# # Detect Cycle in a Directed Graph:

# In[7]:


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[node] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices

        for v in range(self.vertices):
            if not visited[v]:
                if self.is_cyclic_util(v, visited, recursion_stack):
                    return True

        return False


g = Graph(4)  
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)

if g.is_cyclic():
    print("Cycle detected in the directed graph.")
else:
    print("No cycle detected in the directed graph.")


# # Implement n-Queen’s Problem

# In[8]:


def is_safe(board, row, col):
   
    for i in range(col):
        if board[row][i] == 1:
            return False

   
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

   
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_util(board, col):
    
    if col == len(board):
        return True

    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    if solve_n_queens_util(board, 0):
       
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
    else:
        print("No solution exists for the given value of n.")

n = 4
print(f"Solutions for n = {n}:")
solve_n_queens(n)


# In[ ]:




