from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import winsound

screen = Screen()
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkey(screen.bye, "Escape")

is_game_over = False

while not is_game_over and score.l_score < 3 and score.r_score < 3:
    time.sleep(ball.delay_time)
    screen.update()
    ball.move_ball()

    # detect collision with the top walls
    if ball.ycor() > 270 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the left and right paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        winsound.Beep(frequency=3500, duration=3)
        ball.bounce_x()

    # check if right paddle misses
    if ball.xcor() > 340:
        ball.reset_position()
        score.l_point()

    # check if right paddle misses
    if ball.xcor() < -340:
        ball.reset_position()
        score.r_point()

    score.check_winner()
screen.exitonclick()