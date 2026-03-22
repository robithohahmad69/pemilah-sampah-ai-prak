# graph.py
# Menyimpan semua node dan hubungan proses

graph = {
    "M": ["A"],  # Sampah masuk ke sorting

    "A": ["B", "G"],  # Sorting: lanjut atau gagal (kontaminasi)
    "B": ["C"],       # Bersihkan label/tutup
    "C": ["D"],       # Pencacahan
    "D": ["E", "J"],  # Washing: bisa gagal residu
    "E": ["F", "G"],  # Sink-float: bisa gagal kontaminasi
    "F": ["H"],       # Pengeringan
    "H": ["T", "I"],  # Ekstrusi: bisa sukses atau degradasi

    "T": [],  # Goal: plastik food grade
    "G": [],  # Gagal: kontaminasi
    "I": [],  # Gagal: degradasi
    "J": []   # Residu
}