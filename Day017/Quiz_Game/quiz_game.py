from question_model import Question
from qg_data import questions_db
from quiz_brain import QuizBrain

question_bank = []
for _ in questions_db:
    question_ans = Question(_['text'], _['answer'])
    question_bank.append(question_ans)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n")
print("You've completed the quiz.")
print(f"Your final scoree is {quiz.score}/{quiz.q_num}")
