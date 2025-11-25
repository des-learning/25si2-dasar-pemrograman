# buka file
f = open('file-text.py', 'rt')
# baca seluruh baris file ke memory
for i in f.readlines():
    # tampilkan ke stdout
    print(i)
# tutup file
f.close()

## kode yang sama tapi menggunakan context manager
with open('file-text.py', 'rt') as f:
    for i in f.readlines():
        print(i)

## overwrite file text
with open('file-text.txt', 'wt') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent quis orci eu velit dictum venenatis ac vel quam. Pellentesque est lectus, ullamcorper a semper ac, aliquet ac lorem. Nunc vehicula mattis molestie. Integer pharetra dui ac nisi accumsan, eu fermentum diam venenatis. Praesent blandit eros at mollis malesuada. Nunc volutpat nibh ipsum, quis pharetra sem viverra nec. Cras in tristique tellus, sed faucibus mauris. Praesent ultricies, quam et auctor pellentesque, velit ex elementum sem, eu dictum massa ligula ut erat. Morbi et nunc ipsum. Donec bibendum tellus nibh, at ullamcorper nunc sollicitudin vel.')

## append file text
from datetime import datetime
with open('append.txt', 'at') as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))