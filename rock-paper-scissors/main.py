rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
while True:
  user = input("Choose 1 for Paper, 2 for Scissors, or 3 for Rock: ")
  if user not in ["1", "2", "3"]:
    print("Please don't cheat\n")
    break;

  user = int(user)
  cpu = random.randint(1, 3)
  
  if cpu == user:
    print("\nIt's a draw\n")
  elif cpu == 3 and user == 1:
    print("\nYou win!\n")
  elif cpu == 1 and user == 3:
    print("\nYou lose\n")
  elif cpu < user:
    print("\nYou win!\n")
  else:
    print("\nYou lose\n")

  choice = [paper, scissors, rock]
  print(f"CPU:{choice[cpu - 1]}")
  print(f"YOU:{choice[user - 1]}")
  
