#DAYS 41 and 42 - short hand if-else statements, enumerate function
userlist = []
n = int(input("Enter number of elements to add: "))
for i in range(n):
    ele = input("Enter an element: ")
    ele = float(ele) if ele.isalnum() and not ele.isalpha() else ele
    userlist.append(ele)

numberelements = []
stringelements = []
for i in enumerate(userlist, start=1):
    numberelements.append(i[: : -1]) if type(i[1]) == float else stringelements.append(i[: : -1])

numberelements.sort()
stringelements.sort()
print(f"Sorted list of (numeric elements, position they were found in) - {numberelements}")
print(f"Sorted list of (string elements, position they were found in) - {stringelements}")
