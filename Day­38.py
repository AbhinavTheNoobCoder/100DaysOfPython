#DAY 38 - Raising custom errors
class QuitError(Exception):
    pass
x = input("Enter a number between 5 and 9, or enter 'quit': ")
try:
    if x == "quit":
        raise QuitError
    x = int(x)
    if x < 5 or x > 9:
        raise ValueError("You were asked to input a value between 5 and 9.")
    
    def DoubleFactorial(n):
        product = 1
        if n%2 == 0:
            for i in range(2, n+1, 2):
                product *= i
        else:
            for i in range(1, n+1, 2):
                product *= i
        return product

    print(f"{x}!! =", DoubleFactorial(x))

except QuitError:
    print("Successfully quit the program")

