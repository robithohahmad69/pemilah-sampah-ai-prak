# dfs.py

def dfs(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    print("DFS Kunjungi:", start)

    if start == "T":
        print("✅ DFS sampai tujuan:", path)
        return path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, visited, path + [neighbor])
            if result:
                return result

    return None