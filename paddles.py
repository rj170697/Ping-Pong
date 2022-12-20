from turtle import Turtle,Screen
screen=Screen()


class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(0.5,2)
        self.penup()
        self.setheading(90)
        self.goto(-280,0)
    def move_frwrd(self):
        self.forward(10)
    def move_bckwrd(self):
        self.backward(10)
class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(0.5, 2)
        self.penup()
        self.setheading(90)
        self.goto(270, 0)
    def move_frwrd(self):
        self.forward(10)
    def move_bckwrd(self):
        self.backward(10)
