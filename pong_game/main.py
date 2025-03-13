from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard_ = Scoreboard()
Display_screen = Screen()
Display_screen.setup(width=800, height=600)
Display_screen.bgcolor("black")
Display_screen.title("Pong Game")
Display_screen.tracer(0)

r_position = (350, 0)
l_position = (-350, 0)
r_paddle = Paddle(r_position)
l_paddle = Paddle(l_position)
ball = Ball()


Display_screen.listen()
Display_screen.onkey(r_paddle.go_up, "Up")
Display_screen.onkey(r_paddle.go_down, "Down")
Display_screen.onkey(l_paddle.go_up, "w")
Display_screen.onkey(l_paddle.go_down, "s")




    
    




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    Display_screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard_.l_point()
        
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard_.r_point()

Display_screen.exitonclick()