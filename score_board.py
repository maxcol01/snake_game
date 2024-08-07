from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.points}", align="center", font=("Arial", 20, "normal"))

    def add_score(self, points):
        self.clear()
        self.write(f"Score: {points}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()
