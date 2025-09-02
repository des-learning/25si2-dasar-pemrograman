# dict_example.py
# Contoh tipe data DICTIONARY (key-value pairs / pasangan kunci-nilai)

mahasiswa = {
    "nama": "Alice",
    "umur": 21,
    "jurusan": "Informatika"
}

print("Data mahasiswa:", mahasiswa)
print("Tipe data:", type(mahasiswa))

# Mengakses data dengan key
print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa["umur"])

# Menambah key baru
mahasiswa["angkatan"] = 2023
print("Setelah ditambah:", mahasiswa)

