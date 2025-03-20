import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the states data
states_data = pd.read_csv("50_states.csv")
states = states_data["state"].to_list()
guessed_states = []

# Set up the background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Function to display missed states
def show_missed_states():
    missed_states = [state for state in states if state not in guessed_states]
    missed_states_str = "\n".join(missed_states)
    screen.textinput(title="States You Missed", prompt=f"Here are the states you missed:\n{missed_states_str}\nClick OK to exit.")
    screen.bye()

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name any State of U.S.A").title()
    
    if answer_state == "Exit":
        show_missed_states()
        break
    
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = states_data[states_data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# Keep the window open until the user closes it
turtle.mainloop()