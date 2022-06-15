from tkinter import Button, Label, PhotoImage, Tk, Canvas
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
PADDING = 20
CANVAS_HEIGHT = 250
CANVAS_WIDTH = 300


class QuizInterface:

    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=PADDING, pady=PADDING)
        self.score_label = Label(
            text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(
            width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, width=CANVAS_WIDTH - 20, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=PADDING + 30)
        checkmark_img = PhotoImage(file="images/true.png")
        x_img = PhotoImage(file="images/false.png")
        self.true_button = Button(
            padx=PADDING, 
            pady=PADDING, 
            image=checkmark_img, 
            borderwidth=0,
            highlightthickness=0, 
            command=lambda: self.submit("true")
            )
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(
            padx=PADDING, 
            pady=PADDING, 
            image=x_img, 
            borderwidth=0,
            highlightthickness=0, 
            command=lambda: self.submit("false")
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def submit(self, answer):
        is_correct = self.quiz.check_answer(answer)
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"All Done\nYou scored: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(command=self.window.destroy)
