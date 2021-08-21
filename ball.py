from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create()
        self.speed_x = 10
        self.speed_y = 10
        self.ball_speed = 0.1
        self.prev_y = 0

    def create(self):
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(0,0)

    def move(self):
        self.prev_y = self.ycor()
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.speed_x *= -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        self.speed_y *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1

    def get_prev_y(self):
        return self.prev_y