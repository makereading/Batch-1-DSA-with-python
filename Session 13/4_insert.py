import sys

data = [1, 2, 3, 4]

size = sys.getsizeof(data)

print(f'size of data is {size - 56}')

data.insert(1, 5)

size = sys.getsizeof(data)
print(f'size of data is {size - 56}')
