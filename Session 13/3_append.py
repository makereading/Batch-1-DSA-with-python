# Over allocation
# https://github.com/python/cpython/blob/main/Objects/listobject.c
import sys
data = []
res = {}
SIZE_OF_LIST = 56

for itr in range(1000):
    size = sys.getsizeof(data) - SIZE_OF_LIST
    res[size] = len(data)
    data.append(itr)

print(res)
