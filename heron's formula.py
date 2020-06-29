
import cmath
a=int(input("Enter first side of triangle "))
b=int(input("Enter second side of triangel "))
c=int(input("Enter third side of triangle "))
s=(a+b+c)/2
area=cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle",area)

