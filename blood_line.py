from turtle import Turtle


class BloodLine(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("circle")
        self.shapesize(1.5)
        self.pencolor("red4")
        self.fillcolor("black")
        self.pensize(10)
        self.penup()
        self.goto(pos)
        self.pendown()

    def line(self, cordx, cordy, pos):
        self.goto(pos)
        self.clear()
        angle = self.towards(cordx, cordy)
        self.setheading(angle)
        self.heading()
        self.goto(cordx, cordy)
