import logging

logger = logging.getLogger(__name__)

try:
    a = int(input('angka a: '))
    b = int(input('angka b: '))
    c = a / b
    print('C: ', c)
except ValueError:
    print('nilai input salah')
except ZeroDivisionError:
    print('nilai b tidak boleh 0')
except Exception as e:
    logger.error('terjadi kesalahan dalam program')
finally:
    print('program selesai')