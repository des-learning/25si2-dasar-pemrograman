items = []
lagi = True
while lagi:
    # jual barang
    barang = [
        {'nama': 'buku', 'harga': 10000},
        {'nama': 'pena', 'harga': 3000},
        {'nama': 'pensil', 'harga': 2000},
    ]
    for i, b in enumerate(barang):
        print(f"{i+1}. {b['nama']} ({b['harga']})")
    pilihan = int(input(f"Pilih Barang ({1}-{len(barang)}): "))
    barang=barang[pilihan-1]
    print(barang)
    banyak = int(input('Banyak barang: '))
    subtotal = barang['harga'] * banyak
    print('Subtotal: ', subtotal)
    items.append((barang, banyak, subtotal))
    lagi = input('Ada lagi (y/t): ').lower() == 'y'
# hitung total
total = 0
for i in items:
    _, _, subtotal = i
    total += subtotal
pajak = 0.11 * total
grand_total = total + pajak
print('Total: ', total)
print('Pajak (11%): ', pajak)
print('Grand Total: ', grand_total)
