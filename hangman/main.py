import random
import hangman_words
import hangman_art
import replit

chosen_word = random.choice(hangman_words.word_list)
guesses = ""
game_over = False
lives = 6

#Create blanks
display = ["_"] * len(chosen_word)

#Print logo
print(hangman_art.logo)

while "_" in display and not game_over:
  guess = input("Guess a letter: ").lower()

  #Clear cli round
  replit.clear()
  #Reprint logo
  print(hangman_art.logo)

  #Check guessed letter
  guessed = False
  for index, letter in enumerate(chosen_word):
    if letter == guess:
      display[index] = letter
      guessed = True

  #Check if user is wrong.
  if not guessed:
    lives -= 1
    guesses += guess + " "
  
  #Print results
  print(hangman_art.stages[lives])
  print(f"{' '.join(display)}")
  print(f"Wrong guesses: {guesses}")

  #Check if user has run out of lives.
  if lives <= 0:
    game_over = True
    print("You lose.")
    print(f"Answer is \"{chosen_word}\"")
    
if not game_over:
  print("You win!")