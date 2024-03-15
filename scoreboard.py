from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
with open(file="highscore.txt") as file:
    high_score = int(file.read())


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="highscore.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.high_score}", move=False, align="center",
                   font=('Arial', 24, 'normal'))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
