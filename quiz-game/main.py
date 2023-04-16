import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in data.question_data2:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
