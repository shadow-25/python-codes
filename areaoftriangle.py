import math
a=float(input("length of side A:  "))
b=float(input("length of side B:  "))
c=float(input("length of side C:  "))

s=(a+b+c)/2

area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"the Area of given Tringle is {area}")