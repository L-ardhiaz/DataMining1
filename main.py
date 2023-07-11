import numpy as np

# Fungsi untuk menghitung Euclidean distance
def euclidean_distance(x, y):
    return np.sqrt(np.sum(np.square(np.array(x) - np.array(y))))

# Fungsi untuk menghitung Manhattan distance
def manhattan_distance(x, y):
    return np.sum(np.array(x) != np.array(y))

# Data tabel
data = np.array([
    ["excellent", 80, "B"],
    ["fair", 50, "D"],
    ["good", 90, "A"],
    ["excellent", 75, "B"],
    ["fair", 82, "B"],
    ["good", 65, "C"]
])

# Mengubah data keaktifan menjadi atribut ordinal
ordinal_data = {
    "excellent": 3,
    "fair": 2,
    "good": 1
}

# Matriks dissimilarity campuran
dissimilarity_matrix = np.zeros((len(data), len(data)))

# Menghitung dissimilarity untuk setiap pasangan data
for i in range(len(data)):
    for j in range(len(data)):
        # Menghitung dissimilarity untuk atribut keaktifan (ordinal)
        dissimilarity_aktif = euclidean_distance(ordinal_data[data[i][0]], ordinal_data[data[j][0]])

        # Menghitung dissimilarity untuk atribut nilai UAS (numerik)
        dissimilarity_nilai = manhattan_distance(data[i][1], data[j][1])

        # Menghitung dissimilarity untuk atribut Indeks (nominal)
        dissimilarity_indeks = 0 if data[i][2] == data[j][2] else 1

        # Menggabungkan dissimilarity dari ketiga atribut menggunakan Euclidean distance
        dissimilarity = euclidean_distance([dissimilarity_aktif, dissimilarity_nilai, dissimilarity_indeks], [0, 0, 0])

        # Membulatkan nilai dissimilarity menjadi dua digit desimal
        dissimilarity = round(dissimilarity, 2)

        dissimilarity_matrix[i][j] = dissimilarity
print(dissimilarity_matrix)