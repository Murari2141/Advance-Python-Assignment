#  18) Write a Python program to demonstrate the use of super() in inheritance.

class a:
    def info(self):
        return "I am Parent class ."
    
class b(a):
    def info(self):
        print(super().info())
        return "I am Child class ."

obj = b()
print(obj.info())