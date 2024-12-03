"7. Write a Python program to handle exceptions in a calculator. "

try:
    num1 = float(input("Enter Value of Num 1: "))
    num2 = float(input("Enter Value of Num 2:"))
    opretor = input("Enter Your Operation ( + , - , * , / ): ")

    if opretor == '+':
        res = num1 + num2
    elif opretor == '-':
        res = num1 - num2 
    elif opretor == '*':
        res = num1 * num2 
    elif opretor == '/':
        res = num1 / num2
    print(res)
except ZeroDivisionError:
    print("ZeroDivisionError : Division by zero is not allowed.")
except Exception as err:
    print(f"error:{err}")
