from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self, x, y, name, initial_score):
        super().__init__()
        self.score = initial_score
        self.name = name
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x, y)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'{self.name}: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.write_score()

    def decrement_life(self):
        self.score -= 1
        self.write_score()

    def game_over(self):
        self.goto(0, 20)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)

    def win(self):
        self.goto(0, 20)
        self.write('YOU WIN!', move=False, align=ALIGNMENT, font=FONT)

    def get_score(self):
        return self.score
