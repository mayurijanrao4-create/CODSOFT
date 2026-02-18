def calculator():
    #Simple calculator with basic arithmetic operation
    print("\n"+"="*40)
    print("SIMPLE CALCULATOR")
    print("="*40)

    try:
        num1=float(input("Enter first value`"))
        num2=float(input("Enter second value"))
        print("\nOperations:")
        print("1.Addition(+)")
        print("2.Subtraction(-)")
        print("3.Multiplication(*)")
        print("4.Division(/)")
        print("5.Modulus(%)")
        print("6.Power(^)")
        choice=input("Choose operation(1-6)")
        if choice=='1':
            result=num1+num2
            operation="+"
        elif choice==2:
            result=num1-num2
            operetion="-"
        elif choice==3:
            result=num1*num2
            operation="*"
        elif choice==4:
            if num2==0:
                print("Error:Division by Zero")
                return
            result=num1/num2
            operation="/"
        elif choice==5:
            if num2==0:
                print("Error:Modulus by Zero")
                return
            result=num1%num2
            operation="%"
        elif choice==6:
           result=num1**num2 
           operation="^"
        else:
            print("Invalid choice!")
            return
        print(f"n{num1}{operation}{num2}={result}")
    except ValueError:
        print("Error:Please enter the valid numbers")
    print("="*40)
if __name__ == "__main__":
    calculator()

