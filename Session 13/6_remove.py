import sys

data = [1, 2, 3, 4, 5, 6, 7, 8]

size = sys.getsizeof(data)

print(f'total size of data is {size - 56}')

id_last = id(data[-1])
print(id_last)

data.remove(8)
size = sys.getsizeof(data) - 56

print(size, data)

import ctypes
print(ctypes.cast(id_last, ctypes.py_object).value)
