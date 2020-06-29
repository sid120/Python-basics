print("\t\t\t MENU")
print("\t 1. Addition ")
print("\t 2. Subtraction ")
print("\t 3. Multipication ")
print("\t 4. Division ")
choice=int(input("Enter your choice (1-4) "))

if choice==1:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
    result=num1+num2
    print("Result is ",result)
elif choice==2:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
    result=num1-num2
    print("Result is ",result)
elif choice==3:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
    result=num1*num2
    print("Result is ",result)
elif choice==4:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
    if num2==0:
        print("Can not divide by zero")
    else:    
        result=num1/num2
        print("Result is ",result)
else:
    print("INVALID CHOICE")
