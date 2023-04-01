import os, psutil
process = psutil.Process(os.getpid())

# def print_val_1_to_n(n):
#   if n == 0:
#     return 
#   print_val_1_to_n(n-1)
#   print(n)

# print_val_1_to_n(900)
# 12783616


def print_val_1_to_n_tr(n, k):
  if n == 0:
    return
  print(k)
  print_val_1_to_n_tr(n-1, k+1)

print_val_1_to_n_tr(1000, 1)

print(process.memory_info().rss)  # in bytes 
