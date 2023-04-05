import sys

data = [1, 2, 3, 4, 5, 6, 7, 8]

size = sys.getsizeof(data)

print(f'total size of data is {size - 56}')

for _ in range(7):
    data.pop()
    size = sys.getsizeof(data)
    print(f'size of data is {size - 56}', len(data))
