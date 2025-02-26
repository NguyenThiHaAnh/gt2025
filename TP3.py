def create_adjacency_matrix(edges, num_nodes):
    return [[1 if (i + 1, j + 1) in edges else 0 for j in range(num_nodes)] for i in range(num_nodes)]

def inorder_traversal(tree, node):
    if node not in tree or not tree[node]:
        return [node]
    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []
    return left + [node] + right

# Edge list and number of nodes
edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
num_nodes = 8

# Create adjacency matrix
adj_matrix = create_adjacency_matrix(edges, num_nodes)
print("Adjacency Matrix of Graph G:")
for row in adj_matrix:
    print(row)

# Tree structure for traversal
tree = {
    1: [3, 2],
    2: [6, 5],
    3: [4],
    4: [8],
    5: [7],
    6: [],
    7: [],
    8: []
}

# Inorder traversal
node = int(input("\nEnter the node label (x) for inorder traversal: "))
result = inorder_traversal(tree, node)
print(f"Inorder traversal of subtree rooted at node {node}: {result}")
