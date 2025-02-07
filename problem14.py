from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))  # Sort neighbors alphabetically before adding
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    
    if start not in visited:
        visited.append(start)
        for neighbor in sorted(graph[start]):  # Sort neighbors alphabetically before visiting
            dfs(graph, neighbor, visited)
    return visited

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Start from node 'A'
print("BFS Order:", bfs(graph, 'A'))
print("DFS Order:", dfs(graph, 'A'))
