from turtle import Turtle
from blood_line import BloodLine


class Player(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.goto(starting_position)
        self.step = 0
        self.blood_player = BloodLine((-130, 100))

    def move_up(self):
        self.setheading(90)
        self.heading()
        self.forward(80)
        self.step += 1
        self.blood_player.line(self.xcor(), self.ycor(), (-130, 100))

    def move_down(self):
        self.setheading(270)
        self.heading()
        self.forward(80)
        self.step += 1
        self.blood_player.line(self.xcor(), self.ycor(), (-130, 100))

    def move_left(self):
        self.setheading(180)
        self.heading()
        self.forward(80)
        self.step += 1
        self.blood_player.line(self.xcor(), self.ycor(), (-130, 100))

    def move_right(self):
        self.setheading(0)
        self.heading()
        self.forward(80)
        self.step += 1
        self.blood_player.line(self.xcor(), self.ycor(), (-130, 100))
