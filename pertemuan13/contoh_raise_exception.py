class KesalahanNilai(Exception):
    def __init__(self, message):
        super().__init__(message)

def input_nilai():
    nilai = int(input('Nilai: '))
    if nilai < 0 or nilai > 100:
        #raise ValueError('nilai harus 0-100')
        raise KesalahanNilai('nilai harus 0-100')
    return nilai

try:
    nilai = input_nilai()
#except ValueError:
except KesalahanNilai:
    nilai = 'salah'

print('Nilai yang diinput: ', nilai)
