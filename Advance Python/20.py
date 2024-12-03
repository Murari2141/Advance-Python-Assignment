# 20) Write a Python program to show method overriding.

class vehicles:
    def Type(self):
        return "Vehicle Type "
    
class car(vehicles):
    def Type(self):
        return "This is a Car." 

class bike(vehicles):
    def Type(self):
        return "This is a Bike ."

car1 = car()
bike2 = bike()

print(car1.Type())
print(bike2.Type())