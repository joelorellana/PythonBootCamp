from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))
    #print(question_bank[i].text)
    #print(question_bank[i].answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.show_question()

print("The quiz has ended")
print(f"Yor final score is: {quiz.score}/{quiz.question_number}")
