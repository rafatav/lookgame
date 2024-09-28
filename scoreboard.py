from turtle import Turtle

try:
    with open("highest_score.txt", "r", encoding="utf-8") as f:
        high = int(f.readline())
except FileNotFoundError:
    high = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.highest_score = high
        self.color("white")
        self.hideturtle()
        self.penup()
        self.show_text(pos=(-250, 450), specific_score=f"Score: {self.player_score}")
        self.show_text(pos=(200, 450), specific_score=f"Highest Score: {self.highest_score}")

    def show_text(self, pos, specific_score):
        self.clear()
        self.goto(pos)
        self.write(arg=specific_score, align="center", font=("Arial", 25, "normal"))

    def score_up(self):
        self.player_score += 1
