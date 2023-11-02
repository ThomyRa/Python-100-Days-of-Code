class QuizBrain:

    def __init__(self, q_list) -> None:
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.q_num]
        self.q_num += 1
        usr_ans = input(f"Q. {self.q_num}: {current_question.text}. (True/False)?")
        self.check_answer(usr_ans, current_question.answer)

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def check_answer(self, usr_ans, correct_answer):
        if usr_ans.lower() == correct_answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_num}")
        print("\n")
