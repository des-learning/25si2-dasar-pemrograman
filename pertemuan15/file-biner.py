# tulis file biner
with open('file-biner.bin', 'wb') as f:
    data = bytes([128, 50, 200])
    f.write(data)

# baca file biner (sequential)
with open('file-biner.bin', 'rb') as f:
    data = []
    while True:
        b = f.read(1)
        print(b)
        if b == b'':
            break
        data.append(int(b.hex(), 16))
    print(data)

# baca file biner (random)
with open('file-biner.bin', 'rb') as f:
    data = []
    # pindah -1 byte dari posisi end (2)
    f.seek(-1, 2)
    b = f.read(1)
    data.append(int(b.hex(), 16))
    # pindah -3 byte dari posisi sekarang (1)
    f.seek(-3, 1)
    b = f.read(1)
    data.append(int(b.hex(), 16))
    # pindah 1 byte dari posisi start (0)
    f.seek(1, 0)
    b = f.read(1)
    data.append(int(b.hex(), 16))
    print(data)