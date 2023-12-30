#DAY 21 - Function arguments
def GeometricMean(*numbers):
    product = 1
    for i in numbers:
        product = product * i
    return product**(1/len(numbers))

print(GeometricMean(4,6)) #4.898979485566356

def Welcomer(**names):
    message = "Hello, " + names["fname"] + " " + names["mname"] + " " + names["lname"]
    return message

x = Welcomer(fname = input("Enter first name: "), mname = input("Enter middle name: "), lname = input("Enter last name: "))
print(x)