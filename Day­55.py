#Snake Water Gun
import random
result_matrix = [
#Comp:     0       1       2
        ["draw", "win", "lose"], #User selects 0 - Snake
        ["lose", "draw", "win"], #User selects 1 - Water
        ["win", "lose", "draw"], #User selects 2 - Gun
]
mapping = {0: "Snake", 1: "Water", 2: "Gun"}
userwins = compwins = 0

while True:
    usermove = int(input("Enter [0, 1, 2] for [Snake, Water, Gun] respectively: "))
    compmove = random.randint(0, 2)
    print(f"You chose: {mapping[usermove]}.", end= " ")
    print(f"Computer chose: {mapping[compmove]}")
    result = result_matrix[usermove][compmove]
    print(f"You {result}.") if result in ("win", "lose") else print("Draw.")
    if result in ("win", "lose"):
        userwins += 1 if result == "win" else 0
        compwins += 1 if result == "lose" else 0
    print(f"Score: You {userwins} - {compwins} Computer", "\n")

    match input("Quit (Q) or Continue (any other key): ").lower():
        case "q":
            if userwins > compwins:
                print(f"You won the game {userwins} - {compwins}.")
            elif compwins > userwins:
                print(f"You lost the game {userwins} - {compwins}.")
            else:
                print(f"You drew {userwins} - {compwins}.")
            break
        case _:
            print()