from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.write(arg=f"Level: {self.level}", align="center", font=("courier", 20, "normal"))

    def leve_up(self):
        self.level += 1

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("courier", 40, "normal"))


