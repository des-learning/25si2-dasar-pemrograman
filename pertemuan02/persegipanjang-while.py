# perulangan sampai suatu kondisi dipenuhi
panjang = 0 # set panjang ke nilai yang tidak valid
while panjang <= 0: # ulang terus jika panjang tidak valid
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
