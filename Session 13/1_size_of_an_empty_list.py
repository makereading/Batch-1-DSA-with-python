import sys

data = []

size = sys.getsizeof(data)

print(size, sys.getsizeof([]))


# data = [1, 2, 3, 1]
# print(id(data))
#
# for num in data:
#     print(num, id(num))
#

d1 = [1, 2, 3]
d2 = [1, 2, 3]

print(id(d1), id(d2))


t1 = (1, 2, 3)
t2 = (1, 2, 3)

print(id(t1), id(t2))
