import turtle
import pandas

STATE_DATA = pandas.read_csv("50_states.csv")

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Games")

screen.addshape(IMAGE)

turtle.shape(IMAGE)

writer = turtle.Turtle(visible=False)
writer.penup()
writer.speed("fastest")

# unused code to get x and y value of a click location

# def get_mouse_click_coor(x, y):
    # print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

guessing = True
score = 0
correct_guesses = []


while guessing:
    guess = screen.textinput(title=f"{score}/50 States Correct", prompt="Type name of a state").title()
    if guess == "Exit" or guess == "Quit":
        guessing = False
        missed_states = []
        for state in STATE_DATA.state.to_list():
            if state not in correct_guesses:
                missed_states.append(state)
        learn_data = pandas.DataFrame(missed_states)
        learn_data.to_csv("learn.csv")
        break

    if guess not in correct_guesses:
        state_data = STATE_DATA[STATE_DATA.state == guess]
        if len(state_data) != 0:
            writer.goto(int(state_data.x), int(state_data.y))
            writer.write(state_data.state.item())    
            correct_guesses.append(guess)
            score += 1
    if score >= 50:
        guessing = False


# turtle.mainloop() # alternative way to keep screen open
# screen.exitonclick()