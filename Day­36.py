try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    op = input('''Enter the operation you want to perform -
A for Addition
S for Subtraction
M for Multiplication
D for Division
E for Exponentiation
>>> ''').lower()
    if op == "a":
        print(a + b)
    elif op == "s":
        print(a - b)
    elif op == "m":
        print(a * b)
    elif op == "d":
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Division by 0 is not defined.")
    elif op == "e":
        print(a ** b)
except ValueError:
    print("Invalid input.")