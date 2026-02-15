class Question:
    
    def __init__(self, quetion: str, answers: list[str], correct_index: int):
        self._my_quetion = quetion
        self._answers = answers
        self._correct_index = correct_index

    def print_quetion(self):
        print(f"Question: {self._my_quetion}")

        for (i,answer) in enumerate(self._answers,1):
            print(f"{i} - {answer}")

   
    
    def __repr__(self):
        return f"Question: {self._my_quetion}, Answers: {self._answers}"
    
    
    

    def _get_answer_from_user(self):

        answers_num= len(self._answers)

        while True:
            try:
                answer_index = int(input("Enter the number of your answer: "))
                if 1 <= answer_index <= answers_num:
                    return answer_index - 1
                else:
                    print(f"Please enter a number between 1 and {(answers_num)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")