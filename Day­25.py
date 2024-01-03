#DAY 25 - Basic tuple methods
tup = ()
n = int(input("Enter number of tuple elements you want to add: "))
for i in range(n):
    val = input("Enter value of element: ")
    if val.isdigit():
        val = int(val)
    tup += (val, )
print("Here is your original tuple.")
unique = ()
for i in tup:
    if i not in unique:
        unique += (i, )
print("Your tuple only has these unique elements:", unique)