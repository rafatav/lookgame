from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.color("white")

    def write_over(self):
        self.write(arg="GAME OVER", align="center", font=("Arial", 25, "normal"))
