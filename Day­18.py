#DAY 18 - while loop - best suited for running a loop indefinitely
condition = True
while condition:
    i = int(input("Enter the number: "))
    print(i)
    condition = i >= 18
#The above loop is an attempt from my side to emulate the "do-while" loop which doesn't exist
#in python
print("You've printed a number lesser than 18. I'm out.")