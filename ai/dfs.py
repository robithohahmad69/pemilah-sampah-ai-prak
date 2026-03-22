def dfs(graph, start):
    visited = set()
    path = []

    def dfs_recursive(node):
        if node in visited:
            return False

        visited.add(node)
        path.append(node)
        print("DFS Kunjungi:", node)

        # Berhenti di node tujuan ATAU node jalan buntu
        if node == "T" or node == "G" or node == "J":
            print("DFS selesai di:", node, "| Jalur:", " -> ".join(path))
            return True

        for neighbor in graph[node]:
            if dfs_recursive(neighbor):
                return True

        path.pop()
        return False

    dfs_recursive(start)
    return path if path else None