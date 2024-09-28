from turtle import Screen, Turtle
from player import Player
from computer import Computer
import time
from scoreboard import Scoreboard
from game_over import GameOver


STARTING_PLAYER_POSITION = (-130, 100)
STARTING_COMPUTER_POSITION = (130, 100)
step_key = 1

screen = Screen()
screen.setup(768, 1024)
screen.title("LOOK!")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.bgpic("scream.gif")
screen.register_shape("eye.gif")

current_score = Scoreboard()
highest_score = Scoreboard()
over = GameOver()

while True:
    game_is_on = True
    player = Player(STARTING_PLAYER_POSITION)
    # player.shape("eye.gif")
    player.shape("circle")
    player.shapesize(4)
    player.color("moccasin")
    computer = Computer(STARTING_COMPUTER_POSITION)
    # computer.shape("eye.gif")
    computer.shape("circle")
    computer.shapesize(4)
    computer.color("moccasin")

    current_score.show_text(pos=(-200, 450), specific_score=f"Current Score: {current_score.player_score}")
    highest_score.show_text(pos=(200, 450), specific_score=f"Highest Score: {current_score.highest_score}")
    computer.move()

    screen.onkey(fun=player.move_up, key="w")
    screen.onkey(fun=player.move_down, key="s")
    screen.onkey(fun=player.move_left, key="a")
    screen.onkey(fun=player.move_right, key="d")
    time.sleep(1)
    while game_is_on:
        over.clear()
        screen.update()
        time.sleep(0.1)
        if player.step == step_key:
            if (round(player.xcor()), round(player.ycor())) == computer.computer_cor[0]:
                computer.computer_cor.remove((round(player.xcor()), round(player.ycor())))
                step_key += 1
            else:
                over.write_over()
                player.clear()
                computer.clear()
                computer.blood_comp.clear()
                player.blood_player.clear()
                current_score.clear()
                current_score.player_score = 0
                step_key = 1
                computer.step = 0
                computer.penup()
                computer.goto(1800, 0)
                computer.blood_comp.penup()
                computer.blood_comp.goto(1800, 0)
                player.penup()
                player.goto(1800, 0)
                player.blood_player.penup()
                player.blood_player.goto(1800, 0)
                computer.computer_cor.clear()
                game_is_on = False

        if player.step == computer.step:
            current_score.score_up()
            if current_score.player_score > current_score.highest_score:
                current_score.highest_score = current_score.player_score
                with open("highest_score.txt", "w", encoding="utf-8") as f:
                    f.write(str(current_score.highest_score))
            current_score.show_text(pos=(-200, 450), specific_score=f"Current Score: {current_score.player_score}")
            highest_score.show_text(pos=(200, 450), specific_score=f"Highest Score: {current_score.highest_score}")
            computer.move()
            player.step = 0
            step_key = 1
