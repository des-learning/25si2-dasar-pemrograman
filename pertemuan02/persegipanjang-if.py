# versi percabangan (if)
panjang = input("Panjang: ")
panjang = int(panjang)
if panjang <= 0: # jika panjang tidak valid, error
    print('panjang error')
    exit() # keluar dari program/stop

lebar = input("Lebar: ")
lebar = int(lebar)
if lebar <= 0:
    print('lebar error')
    exit()
    
luas = panjang * lebar
print("Luas: ", luas)
