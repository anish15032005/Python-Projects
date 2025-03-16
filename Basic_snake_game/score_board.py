from turtle import Turtle
import os

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # Check if "data.txt" exists, if not create it with a default high score of 0
        if not os.path.exists("data.txt"):
            with open("data.txt", "w") as file:
                file.write("0")

        # Read high score from "data.txt"
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
