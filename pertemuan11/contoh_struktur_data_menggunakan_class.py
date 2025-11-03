# membuat/definisi class
class Mahasiswa:
    # constructor
    def __init__(self, nim, nama, jurusan):
        # isi attribute/property mahasiswa
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class NilaiMataKuliah:
    def __init__(self, kode, nama, sks, nilai):
        self.kode = kode
        self.nama = nama
        self.sks = sks
        self.nilai = nilai

    # method/fungsi
    def nilai_angka(self):
        tabel_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}
        return tabel_nilai.get(self.nilai, 0) # tabel_nilai[nilai]

    def bobot_nilai(self):
        return self.nilai_angka() * self.sks

class KHS:
    def __init__(self, mahasiswa, list_nilai):
        self.mahasiswa = mahasiswa
        self.list_nilai = list_nilai

    def total_bobot_nilai(self):
        total = 0
        for mk in self.list_nilai:
            total = total + mk.bobot_nilai() # total += mk.bobot_nilai()

        return total

    def total_sks(self):
        total = 0
        for mk in self.list_nilai:
            total += mk.sks

        return total

    def index_prestasi(self):
        return self.total_bobot_nilai()/self.total_sks()

def printMahasiswa(mahasiswa):
    print("NIM: ", mahasiswa.nim)
    print("Nama: ", mahasiswa.nama)
    print("Jurusan: ", mahasiswa.jurusan)

# buat object/variable dengan type Mahasiswa (deklarasi)
budi = Mahasiswa("11111", "Budi", "Sistem Informasi")
printMahasiswa(budi)

susi = Mahasiswa("22222", "Susi", "Sistem Informasi")
printMahasiswa(susi)

agus = {'nim': '3333', 'nama': 'Agus', 'jurusan': 'Sistem Informasi'}
print(agus)

print("budi: ", type(budi))
print("susi: ", type(susi))
print("agus: ", type(agus))

nilaiBudi = NilaiMataKuliah(
    '111', 'Dasar Pemrograman', 3, 'A'
)

print('Nilai: ', nilaiBudi.nilai)
print('SKS: ', nilaiBudi.sks)
print('Nilai Angka: ', nilaiBudi.nilai_angka())
print('Bobot Nilai: ', nilaiBudi.bobot_nilai())

khsBudi = KHS(budi, [
    NilaiMataKuliah('1111', 'Dasar Pemrograman', 3, 'A'),
    NilaiMataKuliah('1112', 'Pemrograman Web', 3, 'B'),
    NilaiMataKuliah('1113', 'Basis Data', 4, 'C'),
])

print('Total Bobot nilai: ', khsBudi.total_bobot_nilai())
print('Total sks: ', khsBudi.total_sks())
print('Index prestasi: ', khsBudi.index_prestasi())