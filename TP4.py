import heapq

def create_weighted_adjacency_matrix():
    size = 9
    matrix = [[0] * size for _ in range(size)]
    edges = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 6, 6), (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 9, 2),
        (7, 9, 8),
        (8, 9, 1),
        (9, 8, 7)
    ]
    for u, v, w in edges:
        matrix[u - 1][v - 1] = w
        matrix[v - 1][u - 1] = w
    return matrix

def print_adjacency_matrix(matrix):
    print("Weighted Adjacency Matrix:")
    for row in matrix:
        print(" ".join(f"{cell:2}" for cell in row))

def prim(matrix, start):
    n = len(matrix)
    visited = [False] * n
    min_heap = [(0, start, start)]
    mst, total_weight = [], 0

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if visited[v]:
            continue
        visited[v] = True
        if u != v:
            mst.append((u + 1, v + 1, weight))
            total_weight += weight
        for neighbor in range(n):
            if matrix[v][neighbor] and not visited[neighbor]:
                heapq.heappush(min_heap, (matrix[v][neighbor], v, neighbor))
    return mst, total_weight

def kruskal(matrix):
    n = len(matrix)
    edges = [(matrix[i][j], i, j) for i in range(n) for j in range(i + 1, n) if matrix[i][j]]
    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1

    mst, total_weight = [], 0
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u + 1, v + 1, weight))
            total_weight += weight

    return mst, total_weight

if __name__ == "__main__":
    adj_matrix = create_weighted_adjacency_matrix()
    print_adjacency_matrix(adj_matrix)

    root = int(input("\nEnter the root node for Prim's algorithm (1-9): ")) - 1
    prim_mst, prim_weight = prim(adj_matrix, root)
    print("\nPrim's Algorithm MST:")
    for u, v, w in prim_mst:
        print(f"Edge {u}-{v} with weight {w}")
    print(f"Total Weight (Prim's): {prim_weight}")

    kruskal_mst, kruskal_weight = kruskal(adj_matrix)
    print("\nKruskal's Algorithm MST:")
    for u, v, w in kruskal_mst:
        print(f"Edge {u}-{v} with weight {w}")
    print(f"Total Weight (Kruskal's): {kruskal_weight}")
