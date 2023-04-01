# from memory_profiler import profile

# @profile
def fact(n):
    res = 1
    for itr in range(1, n+1):
        res *= itr
    return res
print(fact(1000))
