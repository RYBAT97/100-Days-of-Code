class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.user_input = 'false'

    def next_question(self):
        self.user_input = input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} "
                                f"(True/False): ")

    def still_has_questions(self):
        if self.user_input.lower() == str(self.questions_list[self.question_number].answer.lower()) and self.question_number != len(self.questions_list):
            self.question_number += 1
            return True
        else:
            return False
