def sum_natural(n):
    if n==1:
        return 1
    return n+sum_natural(n-1)

print("work till N'th value is 998")
while(True):
    num=int(input("Enter the N'th Number: "))
    print(f"sum of 1 to {num} is ", (sum_natural(num)))