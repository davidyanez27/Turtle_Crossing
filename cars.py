from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setposition(random.randrange(300, 800), random.randrange(-250, 250))
        self.left(180)

    def cars_move(self):
        self.reset_position()
        self.forward(10)

    def reset_position(self):
        if self.xcor() < -280:
            self.setposition(300, random.randrange(-250, 250))


    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        return rgb



