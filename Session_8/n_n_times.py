x=int(input("Enter the input")) #o(1)
for iter1 in range(x):#o(n)
    for iter2 in range(x):#o(n)
        print(f"For every {iter1} we run {iter2} times")

#o(n^2)
