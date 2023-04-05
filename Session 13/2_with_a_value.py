import sys

data = [1]

print(sys.getsizeof(1))

size = sys.getsizeof(data)

print(size, sys.getsizeof(data[0]))
