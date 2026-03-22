# ============================================================
# BASE GRAPH: semua node dan koneksi yang mungkin ada
# M=Masuk, A=Sorting, B=Bersih Label, C=Cacah,
# D=Cuci Besar, E=Pisah Jenis, F=Keringkan, G=Grade Rendah,
# H=Peletisasi, I=Degradasi, J=Residu/Sampah, T=Grade Terbaik
# ============================================================
graph = {
    "M": ["A", "D"],
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["E"],
    "D": ["C", "I"],
    "E": ["H", "F", "I"],
    "F": ["G"],
    "G": [],
    "H": ["T"],
    "I": ["J"],
    "J": [],
    "T": []
}


# ============================================================
# GRAPH PER SKENARIO
# Setiap skenario membatasi tetangga node tertentu
# agar BFS/DFS hanya menelusuri jalur yang relevan
# ============================================================
def get_graph_for_scenario(scenario_id):
    base = {
        "M": ["A", "D"],
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["E"],
        "D": ["C", "I"],
        "E": ["H", "F", "I"],
        "F": ["G"],
        "G": [],
        "H": ["T"],
        "I": ["J"],
        "J": [],
        "T": []
    }

    if scenario_id == "1":
        # M-A-B-C-E-H-T: jalur paling lengkap dan standar
        base["M"] = ["A"]
        base["A"] = ["B"]
        base["E"] = ["H"]

    elif scenario_id == "2":
        # M-D-C-E-H-T: masuk jalur cuci langsung, proses berjalan normal
        base["M"] = ["D"]
        base["D"] = ["C"]
        base["E"] = ["H"]

    elif scenario_id == "3":
        # M-A-C-E-T: sudah tersortir, lewati beberapa tahap, langsung ke hasil
        base["M"] = ["A"]
        base["A"] = ["C"]
        base["E"] = ["T"]

    elif scenario_id == "4":
        # M-A-B-C-E-F-G: ditemukan masalah kualitas saat pengeringan
        base["M"] = ["A"]
        base["A"] = ["B"]
        base["E"] = ["F"]

    elif scenario_id == "5":
        # M-D-C-E-I-J: proses cuci massal gagal, muncul polimer asing
        base["M"] = ["D"]
        base["D"] = ["C"]
        base["E"] = ["I"]

    elif scenario_id == "6":
        # M-D-I-J: kondisi plastik sudah rusak parah sejak awal masuk
        base["M"] = ["D"]
        base["D"] = ["I"]

    return base


# ============================================================
# DESKRIPSI SKENARIO (untuk dropdown di frontend)
# ============================================================
SCENARIO_DESCRIPTIONS = {
    "1": "Plastik campuran baru masuk — belum disortir, perlu proses lengkap dari awal.",
    "2": "Plastik seragam jenis, kondisi cukup bersih — siap langsung dicuci massal tanpa sortir manual.",
    "3": "Plastik sudah tersortir rapi — dapat langsung dicacah tanpa perlu pembersihan label.",
    "4": "Plastik tersortir tapi ditemukan sisa zat kimia saat pengeringan — butuh pengecekan ulang kualitas.",
    "5": "Plastik langsung masuk jalur cuci besar — namun kandungan polimer asing belum terdeteksi di awal.",
    "6": "Plastik terlihat kotor parah sejak awal — kondisi fisik diragukan sebelum proses cuci dimulai."
}