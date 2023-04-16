import art
import random
import game_data
from replit import clear

score = 0
accountB = random.choice(game_data.data)
print(art.logo)

def account_info(account):
    """Returns account info in formatted string"""
    return f"{account['name']}, {account['description']} from {account['country']}."

def check_answer(guess, followersA, followersB):
    """Returns true if the guess is correct based on the number of followers"""
    if followersA > followersB:
        return guess == ("a" or "A")
    else:
        return guess == ("b" or "B")

while True:
    accountA = accountB
    accountB = random.choice(game_data.data)

    print("A: " + account_info(accountA))
    print(art.vs)
    print("B: " + account_info(accountB))

    guess = input("Who has more followers? Type 'A' or 'B': ")

    clear()
    print(art.logo)
  
    if check_answer(guess, accountA['follower_count'],
                    accountB['follower_count']):
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        print(f"Sorry. That's wrong. Final score: {score}.")
        break
