# def example():
#     a = 10
#     b = 20
    
#     if a < b:
#         print("b is greater")
#     else:
#         print("a is greater")

# example()
# #function with parameter
# def example(name):
#     print("hello",name)
# example("Aayusha")

# def example1():
#     num1=int (input("enter any number: "))
#     num2=int (input("enter any number: "))
#     if num1>num2:
#         print(num1)
#     else:
#         print(num2)        
# example1()      

# #takes a string and returns the number of characters
# def count(text):
#     return len(text)
# # Taking input
# user = input("Enter a string:")
# result = count(user)
# print("Number of characters:", result)

set_username = "Aayusha Bisunke"
set_password = "aayusha123"

def login():
    while True:
        username = input("Enter the username: ")   
        if username == set_username:
            break
        else:
            print("Incorrect username. Try again.")
    while True:
        password = input("Enter the password: ")
        if password == set_password:
            print("Login successful ")
            break
        else:
            print("Incorrect password. Try again.")

login()

              