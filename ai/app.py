from flask import Flask, render_template, request, jsonify
from graph import get_graph_for_scenario, SCENARIO_DESCRIPTIONS
from bfs import bfs
from dfs import dfs
from heuristic import greedy_bfs, astar

app = Flask(__name__)


# =========================
# HALAMAN UTAMA
# =========================
@app.route("/")
def index():
    return render_template("index.html", scenarios=SCENARIO_DESCRIPTIONS)


# =========================
# API: BFS & DFS
# =========================
@app.route("/run", methods=["POST"])
def run():
    data = request.get_json()
    scenario_id = data.get("pilihan")
    algo = data.get("algo")  # "bfs" atau "dfs"

    start = "M"
    scenario_graph = get_graph_for_scenario(scenario_id)

    if not scenario_graph:
        return jsonify({"error": "Skenario tidak valid"}), 400

    if algo == "bfs":
        path = bfs(scenario_graph, start)
    elif algo == "dfs":
        path = dfs(scenario_graph, start)
    else:
        return jsonify({"error": "Algoritma tidak dikenali"}), 400

    if not path:
        path = [start]

    return jsonify({
        "start": start,
        "algo": algo,
        "path": path
    })


# =========================
# API: GREEDY & A*
# =========================
@app.route("/run_heuristic", methods=["POST"])
def run_heuristic():
    data = request.get_json()
    scenario_id = data.get("pilihan")
    algo = data.get("algo")  # "greedy" atau "astar"

    start = "M"
    scenario_graph = get_graph_for_scenario(scenario_id)

    if not scenario_graph:
        return jsonify({"error": "Skenario tidak valid"}), 400

    if algo == "greedy":
        path = greedy_bfs(scenario_graph, start)
    elif algo == "astar":
        path = astar(scenario_graph, start)
    else:
        return jsonify({"error": "Algoritma tidak dikenali"}), 400

    if not path:
        path = [start]

    return jsonify({
        "start": start,
        "algo": algo,
        "path": path
    })


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)