bulan = int(input('Masukkan data bulan: '))
if bulan < 1 or bulan > 12:
    print('Data bulan salah')
else:
    # if bulan == 1:
    #    print('31 hari')
    # if bulan == 2:
    #    print('28/29 hari')
    # if bulan == 3:
    #    print('31 hari')
    # if bulan == 4:
    #    print('30 hari')
    # if bulan == 5:
    #    print('31 hari')
    # if bulan == 6:
    #    print('30 hari')
    # if bulan == 7:
    #    print('31 hari')
    #if bulan == 8:
    #    print('31 hari')
    #if bulan == 9:
    #    print('30 hari')
    #if bulan == 10:
    #    print('31 hari')
    #if bulan == 11:
    #    print('30 hari')
    #if bulan == 12:
    #    print('31 hari')
    #if bulan in [1,3,5,7,8,10,12]: # list
    #if bulan in (1,3,5,7,8,10,12): # tuple
    #if bulan in set([1,3,5,7,8,10,12]): # set
    if bulan in {1: None, 3: None, 5: None, 7: None, 8: None, 10: None, 12: None}:
        print('31 hari')
    elif bulan == 2:
        print('28/29 hari')
    else:
        print('30 hari')