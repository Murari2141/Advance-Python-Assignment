#  15) Write a Python program to show multiple inheritance .

class A:
    def a(self):
        print("A'  class .")

class B:
    def b(self):
        print("B'class")

class C(A, B):
    def c(self):
        print("C' class")

c_obj = C()
c_obj.a()  
c_obj.b()  
c_obj.c()  