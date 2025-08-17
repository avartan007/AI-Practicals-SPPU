from collections import deque

# Function to take graph input from the user
def create_graph():
    graph = {}
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    
    for i in range(n):
        graph[i] = []

    print("Enter edges (format: u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    return graph

# DFS using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS using queue
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main program
graph = create_graph()
start = int(input("Enter starting node for traversal: "))

print("\nDFS Traversal:")
dfs(graph, start)

print("\n\nBFS Traversal:")
bfs(graph, start)
