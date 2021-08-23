from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def check_winner(self):
        if self.r_score == 3:
            self.goto(0, 0)
            self.write("Right wins", align="Center", font=("Courier", 30, "normal"))
        elif self.l_score == 3:
            self.goto(0, 0)
            self.write("Left wins", align="Center", font=("Courier", 30, "normal"))