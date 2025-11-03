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
