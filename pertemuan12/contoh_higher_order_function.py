# non functional
def genap(data):
    hasil =[]
    for i in data:
        if i % 2 == 0:
            hasil.append(i)
    return hasil

def ganjil(data):
    hasil = []
    for i in data:
        if i % 2 != 0:
            hasil.append(i)
    return hasil

def diakhiri_i(data):
    hasil = []
    for i in data:
        if i[-1] == 'i':
            hasil.append(i)
    return hasil

# pada 3 fungsi di atas ada bagian yang sama dan ada bagian code yang
# berubah sesuai dengan kebutuhan yaitu i % 2 == 0, i % 2 != 0, i[-1] == 'i'
# bagian code tersebut bisa dijadikan parameter, jika hasil evaluasi bernilai
# benar, maka simpan ke hasil
# secara fungsional kode di atas bisa di generalized menjadi
def saring(data, fungsi_saring):
    hasil = []
    for i in data:
        if fungsi_saring(i):
            hasil.append(i)
    return hasil

# lambda disebut juga anonymous function atau function literal
print(saring([1,2,3,4,5,6,7,8,9,10], lambda x: x % 2 == 0)) # saring bilangan genap
print(saring([1,2,3,4,5,6,7,8,9,10], lambda x: x % 2 != 0))
print(saring(['budi', 'agus', 'iwan', 'susi', 'ali'], lambda x: x[-1] == 'i'))

def nilai_diatas_60(x):
    return x > 60

print(saring([100, 70, 30, 40, 60, 40, 30, 20, 50, 80], nilai_diatas_60))
