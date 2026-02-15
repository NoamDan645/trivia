from question import Question
import pathlib
import json
import random

def get_questions_from_file(file_path: str) -> list[Question]:
    
    questions_file = pathlib.Path(file_path)
    
    assert questions_file.exists(), "The file with questions does not exist."
    
    questions_list = json.load(questions_file.open())
    
    return [
        Question(q["question"], q["answers"], q["correctAnswer"]) 
        for q in questions_list
    ]
   

if __name__ == "__main__":
    
    game_quetions = get_questions_from_file("questions.json")
    
    random.shuffle(game_quetions)
    
    for q in game_quetions:
        if q.ask_a_question():
            print("Correct!")
        else:
            print("Wrong!")
         
    



