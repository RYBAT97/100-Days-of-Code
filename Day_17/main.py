from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def initiate(quiz):
    quiz.next_question()
    if quiz.still_has_questions():
        print("You got it right!")
        initiate(quiz)
    else:
        print(f"That is wrong. The correct answer was {str(quiz.questions_list[quiz.question_number].answer)}. "
              f"Score: {quiz.question_number}/{quiz.question_number + 1}")


question_bank = []
for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

my_quiz = QuizBrain(question_bank)

initiate(my_quiz)


