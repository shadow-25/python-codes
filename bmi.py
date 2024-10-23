while(True):
    w=int(input("Enter your weight in Kg: "))
    h=float(input("Enter your height in M: "))
    x=w/(h**2)

    if x<18.5:
        print("Under weight")
    elif x>=18.5 and x<25:
        print("Normal")
    elif x>=25 and x<30:
        print("Over weight")
    else:
        print("Obesity")