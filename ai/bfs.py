from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            print("BFS Kunjungi:", node)

            if node == "T":
                print("✅ BFS sampai tujuan:", path)
                return path  # ✅ WAJIB RETURN PATH

            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None