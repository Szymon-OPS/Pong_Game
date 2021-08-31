#IMPORTS
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#SCREEN
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
#Get rid of initial animation > moving paddle to side
screen.tracer(0)

#CREATE RIGHT(R) / LEFT(L) PADDLE AND MOVEMENT
paddle_R = Paddle((350, 0))
paddle_L = Paddle((-350, 0))

screen.listen()
screen.onkey(paddle_R.move_up, "Up")
screen.onkey(paddle_R.move_down, "Down")
screen.onkey(paddle_L.move_up, "w")
screen.onkey(paddle_L.move_down, "s")

#BALL, movement, wall collision and bounce, collision with paddle, paddle miss and score update
ball = Ball()

score = Scoreboard()
#Update the screen with everything that was created so far:
game_is_on = True
while game_is_on:
    screen.update()
    #Make the ball move
    ball.move()
    #To make ball movement visible - slow down refresh of the screen
    time.sleep(ball.move_speed)

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Detect collision with paddles
    if ball.distance(paddle_R) < 50 and ball.xcor() > 320 or ball.distance(paddle_L) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect if R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        score.l_point()
    #Detect if L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        score.r_point()

screen.exitonclick()