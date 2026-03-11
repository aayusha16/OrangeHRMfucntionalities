# # # # # # # # # # # # #name = input("What is your name? ")
# # # # # # # # # # # # #age = input("What is your age? ")
# # # # # # # # # # # # #print("Hi Your name is " ,name, ".You are" ,age,"years old")
# # # # # # # # # # # # a=12
# # # # # # # # # # # # b=13
# # # # # # # # # # # # print(a==b)
# # # # # # # # # # # # print(a>b)
# # # # # # # # # # # # print(a<b)
# # # # # # # # # # # # print(a!=b)
# # # # # # # # # # # age= 20
# # # # # # # # # # # if (age>20):
# # # # # # # # # # #     print("you can vote")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("you are not eligible")
# # # # # # # # # # # number = input("Enter a number: ")

# # # # # # # # # # # if number % 2 == 0:
# # # # # # # # # # #     print("This number is even")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("This number is odd")

        
# # # # # # # # # # number = input("Enter a number: ")

# # # # # # # # # # if number.isdigit():
# # # # # # # # # #     number = int(number)
    
# # # # # # # # # #     if number % 2 == 0:
# # # # # # # # # #         print("This number is even")
# # # # # # # # # #     else:
# # # # # # # # # #         print("This number is odd")
# # # # # # # # # # else:
# # # # # # # # # #     print("Invalid number")
# # # # # # # # # for loop
# # # # # # # # # fruits = ["Apple","orange","mango"]
# # # # # # # # # for i in range (120):
# # # # # # # # #     print(i)  
    
# # # # # # # #     #while loop
# # # # # # # # count = 0 
# # # # # # # # while count<5:
# # # # # # # #     print(count)
# # # # # # # #     count +=1
    
# # # # # # # # count = 10
# # # # # # # # while count>0:
# # # # # # # #     print(count)
# # # # # # # #     count-=1


# # # # # # # #rtake inpout form useer and check if the input is even or odd and if its not string then show invaslid using while loop.
# # # # # # # while True: #while True =  keeps asking until correct input
# # # # # # #     num= input("Enter a number: ")
    
    
# # # # # # #     if num.isdigit():  
# # # # # # #         number = int(num)
        
        
# # # # # # #         if number % 2 == 0:
# # # # # # #             print("This number is even ")
# # # # # # #         else:
# # # # # # #             print("This number is odd ")
        
# # # # # # #         break  # break = stops loop after valid number
    
# # # # # # #     else:
# # # # # # #         print("Invalid input! Please enter a valid number ")
# # # # # # # name = input("enter your name ")
# # # # # # # def greet():
# # # # # # #     print("Hello", name)

# # # # # # # greet()
# # # # # # def find_largest(num1, num2):
# # # # # #     if num1 > num2:
# # # # # #         print("The largest number is:", num1)
# # # # # #     elif num2 > num1:
# # # # # #         print("The largest number is:", num2)
# # # # # #     else:
# # # # # #         print("Both numbers are equal")

# # # # # # # Taking input
# # # # # # a = int(input("Enter first number: "))
# # # # # # b = int(input("Enter second number: "))

# # # # # # find_largest(a, b)
# # # # # # # Set username and password
# # # # # # set_username = "admin"
# # # # # # set_password = "1234"

# # # # # # # Take input from user
# # # # # # username = input("Enter username: ")
# # # # # # password = input("Enter password: ")

# # # # # # # Check login
# # # # # # if username == set_username and password == set_password:
# # # # # #     print("Login successful ")
# # # # # # else:
# # # # # #     print("Login failed ")



# # # # # #rtake inpout form useer and check if the input is even or odd and if its not string then show invaslid using while loop.
# # # # # while True: #while True =  keeps asking until correct input
# # # # #     num= input("Enter a number: ")
    
    
# # # # #     if num.isdigit():  
# # # # #         number = int(num)
        
        
# # # # #         if number % 2 == 0:
# # # # #             print("This number is even ")
# # # # #         else:
# # # # #             print("This number is odd ")
        
# # # # #         break  # break = stops loop after valid number
    
# # # # #     else:
# # # # #         print("Invalid input! Please enter a valid number ")

# # # # #list 
# # # # numbers = [1,2,3,4,5]
# # # # name = ["ram", "hari", "shyam"]
# # # # mixed =[10, "apple",3.6]

# # # # print(numbers, name , mixed)

# # # # print(numbers[1])

# # # # name[1]= "sita"
# # # # print(name)

# # # # name.append("aayusha")
# # # # print(name)

# # # # name.remove("aayusha")

# # # # name.pop(1) #delete the index num. name only 

# # # # name.clear() #it clears all 

# # # # print(name)




# # # #loop question  1to 100 and showing odd and even too
# count=0
#     while count<100:
#         print(count)
#     count +=1
    
# count = 1
# while count <=100:
#     if count %2 ==0:
#         print(count, "even number")
#     else:
#         print( count, "odd number")
# count+=1        
    
# # count = 0
# #1 to 100 , even and odd
# count = 1

# while count <= 100:
#     if count % 2 == 0:
#         print(count, "- Even")
#     else:
#         print(count, "- Odd")
    
#     count += 1
