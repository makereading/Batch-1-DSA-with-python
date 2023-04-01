import os, psutil
process = psutil.Process(os.getpid())

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    # res = 1
    # for itr in range(1, n+1):
    #     res = res * itr
    # return res
fact(900)

print(process.memory_info().rss)  # in bytes 
