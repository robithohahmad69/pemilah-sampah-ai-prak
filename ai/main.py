from graph import graph
from bfs import bfs
from dfs import dfs


def get_start_node():
    pilihan = input(
        "\n=== PILIH KONDISI SAMPAH ===\n"
        "1. Sampah sesuai kriteria\n"
        "2. Sampah tidak sesuai kriteria\n"
        "3. Bukan sampah plastik\n"
        "Masukkan pilihan (1/2/3): "
    )

    mapping = {
        "1": "M",
        "2": "G",
        "3": "J"
    }

    return mapping.get(pilihan, None)


def run():
    start = get_start_node()

    if not start:
        print("❌ Input tidak valid")
        return

    # BFS & DFS
    bfs_path = bfs(graph, start)
    dfs_path = dfs(graph, start)

    print("\n=== HASIL ===")
    print("BFS Path:", bfs_path)
    print("DFS Path:", dfs_path)




if __name__ == "__main__":
    run()