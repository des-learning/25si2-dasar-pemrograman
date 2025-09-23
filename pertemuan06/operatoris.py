data = [
    10,
    3.14,
    True,
    [1,2,3], 
    set([1,2,3]), 
    (1,2,3),
    {'nama': 'budi', 'umur': 20},
    None
]

for j in data:
    jenis = None
    i = type(j)
    if i is int:
        jenis = 'int'
    elif i is float:
        jenis = 'float'
    elif i is bool:
        jenis = 'boolean'
    elif i is list:
        jenis = 'list'
    elif i is set:
        jenis = 'set'
    elif i is tuple:
        jenis = 'tuple'
    elif i is dict:
        jenis = 'dictionary'
    elif i is None:
        jenis = 'None'
    else:
        jenis = 'tidak diketahui'
    print(j, ' adalah sebuah ', jenis)