import random
print("Welcome to \"Guess The Number.\"")
name = input("Enter your name here: ")
digits = int(input('''Select the range for "Guess The Number".
Press 1 for 0-100
Press 2 for 100-1000
>>> '''))
mode = input('''Which mode do you want to play in?
Press E for Easy
M for Medium
H for Hard
>>> ''')

def Modulus(n):
    if n <= 0:
        return (-1)*n
    else:
        return n

list_of_guesses = []

if digits == 1:
    if mode.lower() == "e":
        chances = 10
    elif mode.lower() == 'm':
        chances = 7
    else:
        chances = 4

    number_to_guess = random.randint(0, 100)

    for i in range(1, chances+1):
        print()
        user_guess = int(input("Guess a number between 0 to 100: "))

        list_of_guesses.append(user_guess)

        if user_guess == number_to_guess:
            print("You won. Congratulations.")
        
            with open("Record.txt", "r") as f:
                file_content = f.read()
                f.seek(65)
                lines = []
                for line in f:
                    if line != "\n":
                        lines.append(line)
                    else:
                        break

                i = str(i) + "\n"
                lines.append(f"{name} - {i}")
                
                list_of_turns = []
                f.close()

            for line in lines:
                name, turn = line.split(" - ")
                list_of_turns.append(turn)

            list_of_turns.sort()
            leaderboard = []

            turn_records = {turn: [] for turn in list_of_turns}

            for line in lines:
                name, turn = line.split(" - ")
                turn_records[turn].append(name)
                
            for turn_record in turn_records:
                names = turn_records[turn_record]
                for name in names:
                    leaderboard.append(f"{name} - {turn_record}")
            
            ldb_1_to_100 = ''.join(leaderboard)
            firstline = file_content[:64]
            lastline = file_content[file_content.index("Leaderboard for Range 100"): ]
            edit = f"{firstline}{ldb_1_to_100}\n{lastline}"
            with open("Record.txt", "w") as file:
                file.write(edit)
                file.close()

            break

        elif user_guess < number_to_guess:
            print("The number is higher than this.")
            print("You have", chances - i, "chances left.")
        else:
            print("The number is lower than this.")
            print("You have", chances - i, "chances left.")
        
        if len(list_of_guesses) > 1:
            if Modulus(number_to_guess - list_of_guesses[-1]) > Modulus(number_to_guess - list_of_guesses[-2]):
                print("Colder.") if i != chances else ""
            else:
                print("Warmer.") if i != chances else ""

        if chances - i == 0:
            print("The number was", number_to_guess)

elif digits == 2:
    if mode.lower() == "e":
        chances = 13
    elif mode.lower() == 'm':
        chances = 10
    else:
        chances = 7

    number_to_guess = random.randint(100, 1000)

    for i in range(1, chances+1):
        print()
        user_guess = int(input("Guess a number between 100 to 1000: "))
        list_of_guesses.append(user_guess)
        if user_guess == number_to_guess:
            print("You won. Congratulations.")
            with open("Record.txt", "r") as f:
                file_content = f.read()
                title = "Leaderboard for Range 100-1000: [Player name - Turns taken to win]\n"
                new_line_count = file_content.count("\n", 0, file_content.index("Leaderboard for Range 100"))
                f.seek(file_content.index("Leaderboard for Range 100") + 1 +  len(title) + new_line_count)
                lines = []
                for line in f:
                    lines.append(line)

                i = str(i) + "\n"
                lines.append(f"{name} - {i}")
                
                list_of_turns = []
                f.close()

            for line in lines:
                name, turn = line.split(" - ")
                list_of_turns.append(turn)

            list_of_turns.sort()
            leaderboard = []

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
                            turn_record = turn_record[:-1]
                    else:
                        if not (i == len(turn_records) and index == len(names)):
                            turn_record += '\n'
                    leaderboard.append(f"{name} - {turn_record}")
                i += 1
            
            ldb_100_to_1000 = ''.join(leaderboard)
            title = "Leaderboard for Range 100-1000: [Player name - Turns taken to win]\n"
            firstline = file_content[:file_content.index("Leaderboard for Range 100") + len(title)]
            edit = f"{firstline}{ldb_100_to_1000}"

            with open("Record.txt", "w") as file:
                file.write(edit)
                file.close()

            break

        elif user_guess < number_to_guess:
            print("The number is higher than this.")
            print("You have", chances - i, "chances left.")
        else:
            print("The number is lower than this.")
            print("You have", chances - i, "chances left.")

        if len(list_of_guesses) > 1:
            if Modulus(number_to_guess - list_of_guesses[-1]) > Modulus(number_to_guess - list_of_guesses[-2]):
                print("Colder.") if i != chances else ""
            else:
                print("Warmer.") if i != chances else ""
        
        if chances - i == 0:
            print("The number was", number_to_guess)