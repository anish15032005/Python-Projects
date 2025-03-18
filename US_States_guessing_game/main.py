import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the states data
states_dataset = pd.read_csv("50_states.csv")
states = states_dataset["state"].to_list()
correct = 0
guessed_states = []

# Set up the background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Main game loop
while correct < 50:
    state = screen.textinput(title=f"{correct}/50 States Correct", prompt="Name any State of U.S.A")
    if state is None:
        break
    state = state.strip().title()  # Convert input to title case
    if state == "Exit":
        missed_states = "\n".join(states)
        screen.textinput(title="States You Missed", prompt=f"Here are the states you missed:\n{missed_states}\nClick OK to exit.")
        screen.bye()  # Close the turtle graphics window
        break
    if state in states:
        guessed_states.append(state)
        states.remove(state)
        correct += 1
        screen.title(f"{correct}/50 States Correct")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_dataset[states_dataset["state"] == state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state)

# Keep the window open until the user closes it
turtle.mainloop()