#DAY 20 - Python functions - User-defined functions
def Factorial(n):
    factorial = 1
    if n == 0:
        factorial = 1
    else:
        for i in range(1, n+1):
            factorial = factorial * i
    return factorial

def Modulus(n):
    if n < 0:
        return ((-1) * n)
    else:
        return n

answer = (100**2)/Factorial(100)
for k in range(2, 101):
    answer += Modulus(((k**2) - (3*k)+ 1)/Factorial(k-1))
print("The answer to your JEE question is =", answer) #Answer is 3