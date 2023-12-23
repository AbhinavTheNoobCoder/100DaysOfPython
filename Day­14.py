#DAY 14 - conditional statements
age = int(input("Enter your age in years: "))
if age >= 18:
    print("You are eligible to vote.")
    drive_license = input("Do you have a driver's license? Press y for yes, n for no: ")
    if drive_license == 'y':
        print("You are eligible to drive as well.")
    elif drive_license == 'n':
        print("You're not allowed to drive legally though.")
    else:
        print("Follow the instructions and give a valid input.")
else:
    print("You're not allowed to vote.")