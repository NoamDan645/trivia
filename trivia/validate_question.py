from pydantic import BaseModel

class ValidateQuestion(BaseModel):
    question: str
    answers: list[str]
    correctAnswer: int

    def print_quetion(self):
            print(f"Question: {self.question}")

            for (i,answer) in enumerate(self.answers,1):
                print(f"{i} - {answer}")
        
    def ask_a_question(self):

            self.print_quetion()

            answer_index = self._get_answer_from_user()

            return answer_index == self.correctAnswer
    
    def _get_answer_from_user(self):
        answers_num = len(self.answers)
        while True:
            try:
                answer_index = int(input("Enter the number of your answer: "))
                if 1 <= answer_index <= answers_num:
                    return answer_index - 1
                else:
                    print(f"Please enter a number between 1 and {answers_num}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def _get_answer_from_user(self):

        answers_num= len(self.answers)

        while True:
            try:
                answer_index = int(input("Enter the number of your answer: "))
                if 1 <= answer_index <= answers_num:
                    return answer_index - 1
                else:
                    print(f"Please enter a number between 1 and {(answers_num)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")