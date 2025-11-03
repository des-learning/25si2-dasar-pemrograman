def input_data():
    harga_satuan = int(input('Harga satuan: '))
    quantity = int(input('Quantity: '))

    total = harga_satuan * quantity
    print('Total: ', total)

try:
    input_data()
except IndexError:
    print('nomor index salah')
except ValueError:
    print('Nilai harga satuan / quantity salah')
except:
    print('general error')
finally:
    print('program berhenti')