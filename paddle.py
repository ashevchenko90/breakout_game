from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.paddle_color = color
        self.create_paddle()
        self.hidden = False
        self.form = 0

    def create_paddle(self):
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color(self.paddle_color)
        self.goto(self.x, self.y)
        self.setheading(180)

    def hide(self):
        self.hideturtle()
        self.hidden = True

    def change_form(self):
        if not self.form:
            self.shape('circle')
            self.form = 1
        else:
            self.shape('square')

    def is_hidden(self):
        return self.hidden

    def left(self):
        self.setheading(180)
        self.forward(20)

    def right(self):
        # paddle.setheading(270)
        self.backward(20)