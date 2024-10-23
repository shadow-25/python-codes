import time
Current_Time=time.strftime('%H:%M:%S')
print(Current_Time)
Current_Hour=time.strftime('%H')
if(Current_Hour >= '4' and Current_Time < '12'):
    print("GOOD MORNING")
elif(Current_Hour >= '12' and Current_Hour < '16'):
    print("GOOD AFTERNOON")
elif(Current_Hour >= '16' and Current_Hour < '20'):
    print("GOOD EVINING")
else:
    print("GOOD NIGHT")
