#DAY 22 - Introduction to Lists
numlist = [i for i in range(1,11)] #list comprehension - list of numbers in range(1,11)
Sum = 0
for i in numlist:
    Sum += i
print(numlist)
average = Sum/len(numlist)
print("Sum of numbers in the list =", Sum)
print("Average of the numbers in list =", average)