#DAY 10 - Taking user input
a = input("Enter your name here: ")
print("Your name is", a)
x = input("Enter number 1: ")
y = input("Enter number 2: ")
print(x + y) #Will return wrong answer due to concantenation (input is taken as str by default)
print(int(x) + int(y)) #gives correct answer unless floating point number is given