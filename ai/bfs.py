from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            print("BFS Kunjungi:", node)

            # Berhenti di node tujuan ATAU node jalan buntu
            if node == "T" or node == "G" or node == "J":
                print("BFS selesai di:", node, "| Jalur:", " -> ".join(path))
                return path

            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None