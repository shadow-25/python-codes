sum=0
while(True):
    num=input("Enter the price: \n")
    if (num!='q'):
        sum=sum+int(num)
        print(f"your sum so far is {sum}")
    else:
        
        print(f"your bill is {sum} \n Thanks for using our calculator")
        break