#DAY 19 - break statement and continue statement
for i in range(1, 100):
    if i%50 == 0:
        break #comes out of the loop
    if i%10 == 0:
        continue #skips the code below it in the for loop
    print(i, end = ", ")
    if i%20 == 0: #never executed because 20%10 = 0 so multiples of 20 are multiples of 10
        print("I don't like this.")

print()
print("Yeah, I quit before 50 ;-;")