# set_example.py
# Contoh tipe data SET (koleksi tidak berurutan, tidak boleh duplikat)

angka_unik = {1, 2, 3, 3, 2}
print("Isi set:", angka_unik)  # duplikat otomatis hilang
print("Tipe data:", type(angka_unik))

# Menambah elemen ke set
angka_unik.add(4)
print("Setelah ditambah:", angka_unik)

