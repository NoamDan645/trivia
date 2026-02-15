import pathlib
import json
import random


from question import Question
from validate_question import ValidateQuestion

def get_questions_from_file(file_path: str) -> list[Question]:
    
    questions_file = pathlib.Path(file_path)
    
    assert questions_file.exists(), "The file with questions does not exist."
    
    questions_list = json.load(questions_file.open())
    
    game_quetions =  [ 
        ValidateQuestion.model_validate(q)
        for q in questions_list
    ]
    return game_quetions
   

if __name__ == "__main__":
    
    game_quetions = get_questions_from_file("questions.json")
    
    random.shuffle(game_quetions)
    
    for q in game_quetions:
        if q.ask_a_question():
            print("Correct!")
        else:
            print("Wrong!")
         
    



