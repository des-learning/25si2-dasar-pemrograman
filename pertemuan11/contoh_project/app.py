# import kuliah.KHS
from kuliah.KHS import KHS
from kuliah.Mahasiswa import Mahasiswa
from kuliah.NilaiMataKuliah import NilaiMataKuliah
# from kuliah import * # import semua namespace di bawah package/module kuliah

def printKHS(khs):
    print('NIM: ', khs.mahasiswa.nim)
    print('Nama: ', khs.mahasiswa.nama)
    print('Jurusan: ', khs.mahasiswa.jurusan)
    for mk in khs.list_nilai:
        print('Mata kuliah: ', mk.kode, mk.nama)
        print('SKS: ', mk.sks)
        print('Nilai: ', mk.nilai)
        print('Bobot: ', mk.bobot_nilai())
    print('total sks: ', khs.total_sks())
    print('index prestasi: ', khs.index_prestasi())

if __name__ == '__main__':
    budi = Mahasiswa('111', 'Budi', 'Sistem Informasi')
    # khs = kuliah.KHS.KHS()
    khs = KHS(budi, [
        NilaiMataKuliah('1111', 'Dasar Pemrograman', 3, 'A'),
        NilaiMataKuliah('1112', 'Pemrograman Web', 3, 'B'),
        NilaiMataKuliah('1113', 'Basis Data', 4, 'C'),
    ])

    printKHS(khs)