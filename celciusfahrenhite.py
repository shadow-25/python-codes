while(True):    
    print("Please Enter c to convert into Celcius OR Enter f to convert into Fahrenhite")
    a=input()
    if a=="c" or a=="C":
        c=int(input("Enter in fahrenhite: "))
        s=5/9*(c-32)
        print(f"Celcius = {s}")
    elif a=="f" or a=="F":
        f=int(input("Enter in celcius: "))
        s=(9/5*f)+32
        print(f"Fahrenhite = {s}")
    else:
        print("Please Enter Right keyword")