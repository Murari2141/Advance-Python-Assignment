#  12) Write a Python program to demonstrate the use of local and global variables in a class.

glbal = "This is a global variable ."

class abc:
    def __init__(self,local):
        self.local = local

    def display(self):
        print(f"global_var : {glbal} , local_var : {self.local}")

obj = abc("This is Local Variables.")
obj.display()

