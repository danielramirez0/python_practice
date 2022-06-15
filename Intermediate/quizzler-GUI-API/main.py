from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = [Question(record["question"], record["correct_answer"]) for record in question_data]

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# mainloop() of tkinter QuizInterface will have issues with this while loop, so it's disabled
# while quiz.still_has_questions():
    # quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
