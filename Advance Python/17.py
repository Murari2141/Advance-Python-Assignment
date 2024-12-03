# 17) Write a Python program to show hybrid inheritance.

class a():
    a = "class a"

class b(a):
    b = "class b"    

class c(a):
    c = "class c"

class d(c,b):
    d = "class d"

obj = d()

print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)