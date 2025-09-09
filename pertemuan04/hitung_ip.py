# program menghitung IP mahasiswa
# input banyak mata kuliah
banyak_mata_kuliah = int(input('Banyak mata kuliah: '))

# input nama mata kuliah, sks dan nilai
# inisialisasi
daftar_nilai = [] # inisialisasi variable untuk menampung nilai
total_nilai = 0
total_sks = 0

for i in range(banyak_mata_kuliah):
    mata_kuliah = input('Mata kuliah: ')
    sks = int(input('SKS: '))
    nilai_angka = int(input('Nilai angka (0-4): '))
    bobot_nilai = sks * nilai_angka

    # simpan data nilai (tuple) ke daftar nilai
    daftar_nilai.append(
        (mata_kuliah, sks, nilai_angka, bobot_nilai)
    )

    # hitung total nilai dari seluruh mata kuliah (nilai * sks)
    total_nilai = total_nilai + bobot_nilai

    # hitung total sks
    total_sks = total_sks + sks

# hitung IP: total nilai / total sks
ip = total_nilai/total_sks

# tampilkan data nilai + ip
print("="*73)
print(f"| {'Mata Kuliah':20} | {'SKS':10} | {'Nilai':10} | {'Bobot Nilai':20} |")
print("="*73)

for item in daftar_nilai:
    print(f"| {item[0]:^20} | {item[1]:10} | {item[2]:10} | {item[3]:20} |")

print("="*73)
print('Total Nilai: ', total_nilai)
print('Total SKS: ', total_sks)
print('IP: ', ip)