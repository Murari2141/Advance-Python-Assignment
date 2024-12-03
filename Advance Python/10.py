"10) Write a Python program to print custom exceptions."

try :
    num1 = int(input("Enter the value of num1 :"))
    num2 = int(input("Enter the value of num2 :"))

    if num2 <= num1:
        print("num1 is greater than num2 .")
except Exception as err:
      print(f"Error: {err}")
    
else:
    raise ValueError(f"num1 is not greater than num2 Value .")
