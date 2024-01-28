#Day 49 - Intro to File Handling
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

with open("Tally.txt", "a") as f:
    f.write(f"\n{name} - {turns_taken}")