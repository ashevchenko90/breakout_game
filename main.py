from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
import time
from score import Score
import random

colors = ['white', 'green', 'red', 'blue', 'yellow', 'purple', 'grey', 'cyan', 'coral', 'brown', 'cornsilk']

WIN_POINTS = 2
WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.bgcolor('black')
screen.setup(WIDTH, HEIGHT)
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle(0, -260, 'white')
ball = Ball()
score = Score(-100, 270, "Result", 0)
life = Score(100, 270, "Life", 3)

quit_key_pressed = False
enemies = []
enemies_hit = 0

def quit_key():
    global quit_key_pressed
    quit_key_pressed = True

for x in range(7):
    for y in range(5):
        new_enemy = Paddle(-360 + 120 * x, 250 - y * 50, random.choice(colors))
        enemies.append(new_enemy)

is_game_on = True
screen.listen()

screen.onkey(paddle.left, 'a')
screen.onkey(paddle.right, 'd')
# screen.onkey(paddle.change_form, 'l')
screen.onkey(quit_key, 'q')

while is_game_on:
    if quit_key_pressed:
        is_game_on = False
    time.sleep(0.1)
    if enemies_hit >= len(enemies):
        is_game_on = False
        score.win()
    if life.get_score() <= 0:
        is_game_on = False
        life.game_over()

    if ball.xcor() < 20 - WIDTH/2 or ball.xcor() > WIDTH/2 - 40:
        ball.bounce_x()
    for enemy in enemies:
        if enemy.distance(ball) < 40 and not enemy.hidden:
            enemy.hide()
            score.update()
            ball.bounce_y()
            enemies_hit += 1
    if ball.distance(paddle) < 40 and ball.ycor() - ball.prev_y <= 0:
        ball.bounce_y()

    if ball.ycor() < - HEIGHT/2:
        ball.reset()
        life.decrement_life()

    screen.update()
    ball.move()

screen.exitonclick()