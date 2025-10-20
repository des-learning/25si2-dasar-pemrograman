# aplikasi kasir untuk menghitung total penjualan
# input item yang dijual + banyak (nama dan harga item ada di dalam list)
# total penjualan = sum dari harga satuan * banyak item
# pajak = 11% dari total penjualan
# grand total = total penjualan + pajak

def pilih_barang():
    barang = [
        {'nama': 'buku', 'harga': 10000},
        {'nama': 'pena', 'harga': 3000},
        {'nama': 'pensil', 'harga': 2000},
    ]
    for i, b in enumerate(barang):
        print(f"{i+1}. {b['nama']} ({b['harga']})")
    pilihan = int(input(f"Pilih Barang ({1}-{len(barang)}): "))
    return barang[pilihan-1]

def jual_barang():
    barang = pilih_barang()
    print(barang)
    banyak = int(input('Banyak barang: '))
    subtotal = barang['harga'] * banyak
    print('Subtotal: ', subtotal)
    return (barang, banyak, subtotal)

def hitung_total(items):
    total = 0
    for i in items:
        _, _, subtotal = i
        total += subtotal
    pajak = 0.11 * total
    grand_total = total + pajak
    return (total, pajak, grand_total)

def program_jual():
    items = []
    lagi = True
    while lagi:
        items.append(jual_barang())
        lagi = input('Ada lagi (y/t): ').lower() == 'y'
    total, pajak, grand_total = hitung_total(items)
    print('Total: ', total)
    print('Pajak (11%): ', pajak)
    print('Grand Total: ', grand_total)

if __name__ == '__main__':
    program_jual()
