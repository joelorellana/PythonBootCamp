class QuizBrain:
    def __init__(self, list):
        self.question_list = list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number <= len(self.question_list)-1

    def show_question(self):
        current_question = self.question_list[self.question_number]
        user_answer= input(f"Q{self.question_number+1}: {current_question.text}: \n")
        self.question_number +=1
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score +=1
        else:
            print("You got it wrong!")
            print(f"The correct answer is {correct_answer}")
        print(f"Actual score: {self.score}/{self.question_number}\n")
