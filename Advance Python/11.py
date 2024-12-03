# 11) Write a Python program to create a class and access the properties of the class using an object.



class car:
    def __init__(self,company,color,model):
        self.company = company
        self.color = color
        self.model = model

    def display(self):
        print(f"Company : {self.company} , Color : {self.color} , Model-Year: {self.model}")


car1 = car("TATA","WHITE",2020)
car1.display()