# perulangan counted (jumlah tertentu)
#for i in [1,2,3]:
#for i in range(1,4):
for i in range(3):
    print("Perulangan ke: ", i+1) # jika pakai range(3) i ditambah 1 supaya nampilnya 1 - 3
    panjang = 0
    while panjang <= 0:
        panjang = input("Panjang: ") # input data ke variable panjang (string)
        panjang = int(panjang) # ubah variable panjang ke angka integer
        if panjang <= 0:
            print('panjang error')

    lebar = 0
    while lebar <= 0:
        lebar = input("Lebar: ")
        lebar = int(lebar)
        if lebar <= 0:
            print('lebar error')
        
    luas = panjang * lebar
    print("Luas: ", luas)
