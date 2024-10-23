def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
def fdiv(a,b):
    return a//b
def exp(a,b):
    return a**b
def inputNum():
    return int(input("Enter the no: "))
def calculate(n):
    match n:
        case 1:
            a=inputNum()
            b=inputNum()
            return print(f"ADDITION of above number is : " ,(sum(a,b)))
        case 2:
            a=inputNum()
            b=inputNum()
            print(f" SUBTRACTION of above number is : " ,(sub(a,b)))
        case 3:
            a=inputNum()
            b=inputNum()
            return print(f"MULTIPICATION of above number is : " ,(mul(a,b)))
        case 4:
            a=inputNum()
            b=inputNum()
            return print(f"DIVISION of above number is : " ,(div(a,b)))
        case 5:
            a=inputNum()
            b=inputNum()
            return print(f"REMINDER of above number is : " ,(rem(a,b)))
        case 6:
            a=inputNum()
            b=inputNum()
            return print(f"FLOOR DIVISION of above number is : " ,(fdiv(a,b)))
        case 7:
            a=inputNum()
            b=inputNum()
            return print(f"EXPONENTIAL value of above number is : " ,(exp(a,b)))
        case _:
            return print("Enter betweeen 1 - 7")
print("Welcome To Python Calculator")
print("Click 0 to exit from Calculator")
print("Click 1 for ADDITION")
print("Click 2 for SUBTRACTION")
print("Click 3 for MULTIPICATION")
print("Click 4 for DIVISION")
print("Click 5 for REMINDER")
print("Click 6 for FLOOR DIVISION")
print("Click 7 for EXPONENTIAL")
flag=True
while(flag):
    n=inputNum()
    if(n==0):
        break
    else:
        calculate(n)
print("Thank for using This Calculater")