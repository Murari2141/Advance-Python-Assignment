# 16) Write a Python program to show hierarchical inheritance. 
class a():
    a = "Class a"

class b1(a):
    b1 = "Class b1"    

class b2(a):
    b2 = "class b2"

class c1(b1):
    c1 = "class c1"

class c2(b1):
    c2 = "class c2"

obj = c2()

print(obj.a)
print(obj.b1)
print(obj.c2)