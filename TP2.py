from collections import defaultdict, deque

def create_adjacency_matrix(graph, n):
    return [[1 if j + 1 in graph.get(i + 1, []) else 0 for j in range(n)] for i in range(n)]

def convert_to_undirected(graph):
    undirected = defaultdict(set)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            undirected[node].add(neighbor)
            undirected[neighbor].add(node)
    return undirected

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def find_weakly_connected_components(graph, n):
    undirected_graph = convert_to_undirected(graph)
    visited = set()
    components = 0
    for node in range(1, n + 1):
        if node not in visited:
            bfs(undirected_graph, node, visited)
            components += 1
    return components

def dfs(graph, node, visited, stack=None):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, stack)
    if stack is not None:
        stack.append(node)

def transpose_graph(graph):
    transposed = defaultdict(list)
    for src, neighbors in graph.items():
        for dest in neighbors:
            transposed[dest].append(src)
    return transposed

def find_strongly_connected_components(graph, n):
    visited = set()
    stack = []
    for node in range(1, n + 1):
        if node not in visited:
            dfs(graph, node, visited, stack)

    transposed = transpose_graph(graph)
    visited.clear()
    components = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            dfs(transposed, node, visited)
            components += 1
    return components

# Graph definition
graph = {
    1: [2, 4],
    2: [3, 6],
    3: [],
    4: [],
    5: [4, 9, 5],
    6: [3, 4],
    7: [3, 5, 6, 8],
    8: [3, 9],
    9: []
}

n = 9
adj_matrix = create_adjacency_matrix(graph, n)
weakly_connected_components = find_weakly_connected_components(graph, n)
strongly_connected_components = find_strongly_connected_components(graph, n)

print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

print("\nNumber of Weakly Connected Components:", weakly_connected_components)
print("Number of Strongly Connected Components:", strongly_connected_components)
