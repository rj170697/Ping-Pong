from turtle import Screen
from paddles import Paddle1,Paddle2
from ball import Ball
import time
from score_board import Score_board
import random
screen=Screen()

screen.setup(600,600)
ball=Ball()

score_board=Score_board()
paddle1=Paddle1()
paddle2=Paddle2()
screen.listen()
screen.onkeypress(paddle1.move_frwrd,'w')
screen.onkeypress(paddle1.move_bckwrd,'s')
screen.onkeypress(paddle2.move_frwrd,'8')
screen.onkeypress(paddle2.move_bckwrd,'2')
while True:
    time.sleep(0.1)
    screen.update()


    if ball.distance(paddle1)<15 or ball.distance(paddle2)<15:
        ball.impact_paddle()
    elif ball.ycor()>300 or ball.ycor()<-300:
        ball.impact_wall()

    elif ball.xcor()>300:
        score_board.score_addl()
        ball.setagain()
        score_board.score_update()
    elif ball.xcor()<-300:
        score_board.score_addr()
        ball.setagain()
        score_board.score_update()
    ball.move()

    #ball.impact_wall()


screen.exitonclick()













