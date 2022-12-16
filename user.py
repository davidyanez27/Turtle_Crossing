from turtle import Turtle
MOVE_DISTANCE = 10


class User(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(x=0, y=-280)





