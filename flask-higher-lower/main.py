from flask import Flask
import random

number = 0
app = Flask("__main__")


@app.route("/")
def home():
    global number
    number = random.randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>" \
           '<image src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="480" height="480">'


@app.route("/<int:guess>")
def guess_number(guess):
    global number
    if guess > number:
        return f"<h1 style='color:red'>Too high</h1>" \
               '<image src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="480" height="480">'
    elif guess < number:
        return f"<h1 style='color:red'>Too low</h1>" \
               '<image src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="480" height="480">'
    else:
        number = random.randint(0, 9)
        return f"<h1 style='color:green'>You found me!</h1>" \
               '<image src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="480" height="480">'


if __name__ == "__main__":
    app.run(debug=True)
