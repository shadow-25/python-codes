def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fun(n-2)+fun(n-1)

n=int(input("Enter the term: "))
x=fun(n)
print(f"The Fibonacci sequence at {n}th term is {x}")