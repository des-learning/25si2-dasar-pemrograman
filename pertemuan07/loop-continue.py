data = [
    {'nama': 'budi', 'umur': 20, 'jenis_kelamin': 'pria'},
    {'nama': 'agus', 'umur': 35, 'jenis_kelamin': 'pria'},
    {'nama': 'susi', 'umur': 35, 'jenis_kelamin': 'wanita'},
    {'nama': 'amir', 'umur': 27, 'jenis_kelamin': 'pria'},
    {'nama': 'tuti', 'umur': 20, 'jenis_kelamin': 'wanita'},
    {'nama': 'rita', 'umur': 23, 'jenis_kelamin': 'wanita'},
    {'nama': 'ali', 'umur': 26, 'jenis_kelamin': 'pria'},
]

# tampilkan semua
#for i in data:
#    print(i)

# tampilkan yang jenis_kelamin pria
#for i in data:
#    if i['jenis_kelamin'] != 'pria':
#        continue
#    print(i)

# tampilkan yang wanita berumur di bawah 25
for i in data:
    if i['jenis_kelamin'] != 'wanita':
        continue
    if i['umur'] >= 25:
        continue
    print(i)