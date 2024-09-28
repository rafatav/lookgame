from turtle import Turtle, Screen
from blood_line import BloodLine
import random
import time

turn_text = Turtle()


def turn(text, pos):
    turn_text.clear()
    turn_text.hideturtle()
    turn_text.penup()
    turn_text.goto(pos)
    turn_text.color("white")
    turn_text.write(arg=text, align="center", font=("Arial", 10, "bold"))


class Computer(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.computer_cor = []
        self.penup()
        self.goto(starting_position)
        self.step = 0
        self.blood_comp = BloodLine((130, 100))

    def move(self):
        turn("MY TURN!", (25, -170))
        self.step += 1
        for _ in range(self.step):
            Screen().update()
            time.sleep(1)
            if self.xcor() > 360:
                self.setheading(random.choice([90, 180, 270]))
            elif self.xcor() < -100:
                self.setheading(random.choice([0, 90, 270]))
            elif self.ycor() > 490:
                self.setheading(random.choice([0, 180, 270]))
            elif self.ycor() < - 490:
                self.setheading(random.choice([0, 90, 180]))
            else:
                self.setheading(random.choice([0, 90, 180, 270]))
            self.heading()
            self.forward(80)
            self.computer_cor.append((round(self.xcor()) - 260, round(self.ycor())))
            self.blood_comp.line(self.xcor(), self.ycor(), pos=(130, 100))
        turn("your turn", (25, -170))

