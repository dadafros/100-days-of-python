from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.configure(bg=THEME_COLOR, padx=50, pady=50)
        self.window.title("Quizz Brain")

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, text="", width=280, justify="center",
                                                   font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.button_true = Button(image=true_image, borderwidth=0, highlightthickness=0, bg=THEME_COLOR,
                                  activebackground=THEME_COLOR, command=self.true_callback)
        self.button_true.grid(row=2, column=1, padx=20, pady=20)
        self.button_false = Button(image=false_image, borderwidth=0, highlightthickness=0, bg=THEME_COLOR,
                                   activebackground=THEME_COLOR, command=self.false_callback)
        self.button_false.grid(row=2, column=0, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, font=("Arial", 20, "bold"), fg="white")
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.update_text_canvas(self.quiz.next_question())

        self.window.mainloop()

    def true_callback(self):
        self.canvas_color_flash(self.quiz.check_answer("True"))
        self.update_score(self.quiz.score)

    def false_callback(self):
        self.canvas_color_flash(self.quiz.check_answer("False"))
        self.update_score(self.quiz.score)

    def update_text_canvas(self, text):
        self.canvas.configure(bg="light gray")
        if text:
            self.canvas.itemconfig(self.canvas_text, text=text)
            self.button_true.configure(state="active")
            self.button_false.configure(state="active")
        else:
            self.update_text_canvas(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.button_true.configure(state="disabled")
            self.button_false.configure(state="disabled")

    def update_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    def canvas_color_flash(self, answer_is_correct):
        if answer_is_correct:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        question = self.quiz.next_question()
        self.button_true.configure(state="disabled")
        self.button_false.configure(state="disabled")
        self.window.after(1000, self.update_text_canvas, question)
