from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()



def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)#when we use a function as an argument, we don't use parentheses
screen.exitonclick()