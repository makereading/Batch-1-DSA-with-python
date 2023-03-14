
x=int(input("Enter input"))#o(1)3
for iter1 in range(x+1):#o(n)
    iter2=1#o(1)
    while (iter2<=iter1):    #o(logn)    
        print(f"For every {iter1} we run {iter2} times")
        iter2=iter2*2

#o(nlogn)




