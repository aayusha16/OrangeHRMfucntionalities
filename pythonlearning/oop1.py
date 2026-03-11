#Default cobnstructor
class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

car = Car()

print(car.make)
print(car.model)
print(car.year)

#Parameterized constructor 
class Student:
    def __init__(self,name):# builtin constructor 
        self.name=name
    def greet(self): #this is method
        print("Hello, my name is", self.name)
S1 = Student("Aayusha")      
S1.greet() 


class Student:
    def getName(self,name):#user made constructor
        self.name=name
    def greet(self): #this is method
        print("Hello, my name is", self.name)
S1 = Student()  
S1.getName("Aayusha")    
S1.greet()


#login functionalities using OOP:

class Login:
    
    def __init__(self):
        self.username1 = "Aayusha Bisunke"
        self.password1 = "aayusha123"
    def login(self):
        while True:
            username = input("Enter Username: ")
            
            if username == self.username1:
                break
            else:
                print("Login failed. Incorrect username.")
        
        # Password loop
        while True:
            password = input("Enter Password: ")
            
            if password == self.password1:
                print("Login successful ")
                break
            else:
                print("Invalid password. Try again.")
user = Login()
user.login()



   