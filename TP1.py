def check_path(graph, start_node, end_node):
   
    checked_nodes = set()

    def dfs(node):
        if node == end_node:
            return True
        checked_nodes.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in checked_nodes:
                if dfs(neighbor):
                    return True
        return False

    return dfs(start_node)


graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [6],
    6: []
}

start_node = int(input("Enter the start node: "))
end_node = int(input("Enter the end node: "))

if check_path(graph, start_node, end_node):
    print(f"There have path exists between {start_node} and {end_node}.")
else:
    print(f"There is no path exists between {start_node} and {end_node}.")
