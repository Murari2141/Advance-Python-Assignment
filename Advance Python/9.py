"9.Write a Python program to handle file exceptions and use the finally block for closing the file."

try :

    x=10
    y=int(input("Enter Value of B : "))
    result=x/y

except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero is not allowed.")
else :
  print(result)
finally:
    print("This block will always execute.")

