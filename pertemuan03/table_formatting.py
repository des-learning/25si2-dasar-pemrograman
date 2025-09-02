# table_format.py
# Contoh menampilkan data tabel tanpa library tambahan

# Data mahasiswa
data = [
    ["Alice", 21, "Informatika"],
    ["Budi", 22, "Sistem Informasi"],
    ["Citra", 20, "Teknik Komputer"]
]

# {:<10} artinya rata kiri dengan lebar 10 karakter
# {:>5}  artinya rata kanan dengan lebar 5 karakter
# {:^20} artinya rata tengah dengan lebar 20 karakter

# Header
print(f"{'Nama':<10} {'Umur':<5} {'Jurusan':<20}")
print("-" * 35)

# Isi data
for row in data:
    print(f"{row[0]:<10} {row[1]:<5} {row[2]:<20}")

