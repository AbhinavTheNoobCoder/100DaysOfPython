#DAY 30 - Recursions
def FibonacciSequence(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (FibonacciSequence(n-1) + FibonacciSequence(n-2))

number = int(input("Enter which term of the Fibonacci Sequence you want: "))
print("The number is", FibonacciSequence(number))
sequence = [FibonacciSequence(i) for i in range(1, number + 1)]
print("The sequence till here is", sequence)