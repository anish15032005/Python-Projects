from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.color("gray")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)


def move_cw():
    tim.right(10)
    
def move_ccw():
    tim.left(10)
    
def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()

screen.onkey(key="w", fun=move_forwards)#when we use a function as an argument, we don't use parentheses
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_cw)
screen.onkey(key="a", fun=move_ccw)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
