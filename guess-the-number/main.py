#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
from random import randint

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print(art.logo)

level = int(input("Choose the level of difficulty, 1 for Easy, 2 for Hard: "))

if level == 2:
    attempts = HARD_LEVEL_ATTEMPTS
else:
    attempts = EASY_LEVEL_ATTEMPTS

number = randint(1, 100)
number_guess = 0

print("I'm thinking of a number between 1 and 100")

while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    number_guess = int(input("Make a guess: "))
    if attempts == 0:
        print(f"You lose. The answer was {number}")
        break
    elif number_guess > number:
        print("Too high.")
    elif number_guess < number:
        print("Too low.")
    elif number_guess == number:
        print("You got it!")
        break
    attempts -= 1