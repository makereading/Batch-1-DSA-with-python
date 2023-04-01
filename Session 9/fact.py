# from memory_profiler import profile

# @profile    
def fact(n):
    # Base Condition
    if (n <= 1):
        return 1
    else:
        return n * fact(n - 1)

print(fact(100))