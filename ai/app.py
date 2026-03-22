from flask import Flask, render_template, request, jsonify
from graph import graph
from bfs import bfs
from dfs import dfs

app = Flask(__name__)

# =========================
# HALAMAN UTAMA
# =========================
@app.route("/")
def index():
    return render_template("index.html")


# =========================
# API UNTUK BFS & DFS
# =========================
@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    pilihan = data.get("pilihan")

    # Mapping input ke node awal
    mapping = {
        "1": "M",  # Sampah sesuai
        "2": "G",  # Tidak sesuai → langsung gagal
        "3": "J"   # Bukan plastik → residu
    }

    start = mapping.get(pilihan)

    if not start:
        return jsonify({
            "error": "Input tidak valid"
        }), 400

    # Jalankan BFS & DFS dari Python
    bfs_path = bfs(graph, start)
    dfs_path = dfs(graph, start)

    # =========================
    # FIX: HANDLE PATH KOSONG
    # =========================
    if not bfs_path:
        bfs_path = [start]

    if not dfs_path:
        dfs_path = [start]

    # =========================
    # RESPONSE KE FRONTEND
    # =========================
    return jsonify({
        "start": start,
        "bfs": bfs_path,
        "dfs": dfs_path
    })


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)