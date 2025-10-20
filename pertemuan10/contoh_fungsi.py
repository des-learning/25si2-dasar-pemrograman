# definisi sebuah fungsi
def hello():
    print('Hello world')

# fungsi dengan sebuah parameter
def sayHello(name):
    print('======')
    print('Hello, ' + name)
    print('======')

# nama = input('Input nama: ')
# sayHello(nama)
#sayHello(input('Input nama: '))

# n adalah global variable
n = 10
def n_kali(x):
    return n * x

def nilai():
    # x adalah local variable
    x = 100
    return x

# baris ini akan error karena variable x tidak terdefinisi
# variable x di atas hanya di kenal pada fungsi nilai (local scope)
# print(x)

def nilai10():
    pass    # no operation

if __name__ == '__main__':
    # call/jalankan fungsi
    hello()
    sayHello('Susi')
    sayHello('Budi')
    print(n_kali(2))
    print(nilai())
    print(nilai10())