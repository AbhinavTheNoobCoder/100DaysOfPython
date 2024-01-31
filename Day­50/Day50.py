#Day 50 - readlines(), readline() and writelines()
import random
number_to_guess = random.randint(1, 100)
turns_taken = 0
name = input("Enter your name: ")
while True:
    turns_taken += 1
    user_guess = int(input("Guess a number between 1 to 100: "))
    if user_guess == number_to_guess:
        print("You guessed it.")
        break
    elif user_guess < number_to_guess:
        print("Go higher.")
    else:
        print("Go lower.")

with open("Record.txt", "a") as f:
    f.write(f"\n{name} - {turns_taken}")
    f.close()

leaderboard = []
with open("Record.txt", "r") as f:
    lines = f.readlines()
    list_of_turns = []

    for line in lines:
        name, turn = line.split(" - ")
        list_of_turns.append(turn)

    list_of_turns.sort()

    turn_records = {turn: [] for turn in list_of_turns}

    for line in lines:
        name, turn = line.split(" - ")
        turn_records[turn].append(name)

    i = 1    
        
    for turn_record in turn_records:
        names = turn_records[turn_record]
        for index, name in enumerate(names, start=1):
            if "\n" in turn_record:
                if i == len(turn_records) and index == len(names):
                    turn_record = turn_record[: -1]
                    leaderboard.append(f"{name} - {turn_record}")
                else:
                    leaderboard.append(f"{name} - {turn_record}")

            else:
                turn_record = turn_record + '\n' if not\
                    (i == len(turn_records) and index == len(names)) else turn_record
                leaderboard.append(f"{name} - {turn_record}")
        i += 1

    f.close()

with open("Record.txt", "w") as f:
    f.writelines(leaderboard)
