#f-strings
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hi {name}, you will be 100 years old by {2024 - age + 100}.")
birthyear_statement = "{0} was born in the year {2} or {1} (I don't know your exact birth date)"
print(birthyear_statement.format(name, 2024 - age, 2024 - age - 1))
#I like f"" more than string.format() :D