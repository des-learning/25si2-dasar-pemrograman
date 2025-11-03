class Mahasiswa:
    # constructor
    def __init__(self, nim, nama, jurusan):
        # isi attribute/property mahasiswa
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

if __name__ == '__main__':
    print(Mahasiswa('1111', 'Susi', 'Sistem Informasi'))