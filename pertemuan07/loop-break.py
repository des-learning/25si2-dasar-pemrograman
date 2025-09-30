data = [
    {'nama': 'budi', 'umur': 20, 'jenis_kelamin': 'pria'},
    {'nama': 'agus', 'umur': 35, 'jenis_kelamin': 'pria'},
    {'nama': 'susi', 'umur': 35, 'jenis_kelamin': 'wanita'},
    {'nama': 'amir', 'umur': 27, 'jenis_kelamin': 'pria'},
    {'nama': 'tuti', 'umur': 20, 'jenis_kelamin': 'wanita'},
    {'nama': 'rita', 'umur': 23, 'jenis_kelamin': 'wanita'},
    {'nama': 'ali', 'umur': 26, 'jenis_kelamin': 'pria'},
]

cari = input('Input nama yang di cari: ')
data_ketemu = None
for i in data:
    print('cari data di ', i)
    if i['nama'] == cari:
        print('data ketemu! stop pencarian')
        data_ketemu = i
        # break

if data_ketemu is None:
    print('Data tidak ditemukan')
else:
    print(data_ketemu)