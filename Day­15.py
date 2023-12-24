#DAY 15 - Exercise 2 - Greeting user based on time
import time
user = input("Enter your name: ")
timestamp = int(time.strftime('%H'))
if timestamp == 0:
    print("It's midnight,", user)
elif timestamp <= 4:
    print("It's early morning,", user)
elif timestamp <= 7:
    print("You're an early riser. Good morning,", user)
elif timestamp < 12:
    print("Good morning,", user)
elif timestamp < 18:
    print("Good afternoon,", user)
elif timestamp <= 20:
    print("Good evening,", user)
else:
    print("Good night,", user)