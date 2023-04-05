from tail_recursive import tail_recursive
import os, psutil
process = psutil.Process(os.getpid())

# @tail_recursive
# def factorial(n, var=1):
#     if n == 0:
#         return var
#     return factorial.tail_call(n-1, var=var*n)

# val = factorial(1000)
# print(val)

def factorial(n, var=1):
    if n == 0:
        return var
    return factorial(n-1, var=var*n)

factorial(1000)

# print(process.memory_info().rss)  # in bytes 
