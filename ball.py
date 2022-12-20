from turtle import Turtle
import random
from score_board import Score_board
score_board=Score_board()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        #self.setheading(random.choice(range(0,360)))
        self.speed(2)
        self.x_move=10
        self.y_move=10
    def move(self):
        x=self.xcor() + self.x_move
        y=self.ycor()+self.y_move
        self.goto(x,y)
    def impact_wall(self):
        self.y_move=-1*self.y_move
    def impact_paddle(self):
        self.x_move=-1*self.x_move


    def setagain(self):
       self.setheading(random.choice(range(0, 360)))
       self.goto(0,0)