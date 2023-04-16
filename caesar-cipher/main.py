import art
import replit

def ceasar(text, shift):
  result = ""
  for char in text:
    if char.isalpha():
      cipher = ord(char) + shift
      if (char.islower() and chr(cipher).islower()) or \
      (char.isupper() and chr(cipher).isupper()):
        result += chr(cipher)
      else:
        if shift > 0:
          result += chr(cipher - 26)
        else:
          result += chr(cipher + 26)
    else:
      result += char
  return result

go_again = "y"
print(art.logo)

while go_again == "y":
  #User inputs
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))

  #Handles large shifts
  shift = shift % 26
  
  #Calls ceasar function
  if direction == "encode":
    print(f"Here\'s the encoded message: {ceasar(text, shift)}")
  elif direction == "decode":
    print(f"Here\'s the decoded message: {ceasar(text, -shift)}")
  else:
    print("Invalid function choice. Chose encode or decode")

  #Option to terminate program
  go_again = input("Do you want to go again? (y/n) ")

  #Clear and reprint logo
  replit.clear()
  print(art.logo)
  
  
