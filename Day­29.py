#DAY 29 - Docstrings, Zen of Python
print("Haha hold this poem called Zen of Python")
import this #relatable poem
def Factorial(n):
    '''Takes a number and prints its factorial''' #docstring
    if n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n+1):
            product = product * i
        return product
print(Factorial.__doc__) #docstring
number = int(input("Enter a number: "))
print("Factorial of the number =", Factorial(number))