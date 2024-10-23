while(True):   
    t=int(input("Enter total no. of integer:  "))
    y=0
    for i in range(t):
        x=float(input("Enter the no.:  "))
        y=y+x
    avg=y/t

    print(f"Average of given no. is {avg}")