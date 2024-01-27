#DAY 48 - Global variables, local variables and global keyword
counter = 0
def IncrementCounter():
    global counter
    counter += 1
def DecrementCounter():
    global counter
    counter -= 1
def ResetCounter():
    global counter
    counter = 0
while True:
    print(f"Current count: {counter}")
    action = input("Increment (I), Decrement (D), Reset(R) or Stop(S): ").upper()
    if action == "I":
        IncrementCounter()
    elif action == "D":
        DecrementCounter()
    elif action == "R":
        ResetCounter()
    elif action == "S":
        break
    else:
        print("Action unrecognised.")
    print()