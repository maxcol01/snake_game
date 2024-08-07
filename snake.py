from turtle import Turtle

XDIST = 20


class Snake:
    def __init__(self):
        self.y_cor_turtles = []
        self.x_cor_turtles = []
        self.is_on = True
        self.all_turtles = []
        self.x_ref = 0

    def initialize(self):
        for _ in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(0, 0)
            self.all_turtles.append(new_turtle)

        for item in range(0, len(self.all_turtles)):
            self.all_turtles[item].setx(self.x_ref)
            self.x_ref -= XDIST

    def move_snake(self):
        self.x_cor_turtles = []
        self.y_cor_turtles = []
        for nr_snake in range(0, len(self.all_turtles) - 1):
            self.x_cor_turtles.append(self.all_turtles[nr_snake].xcor())
            self.y_cor_turtles.append(self.all_turtles[nr_snake].ycor())

        # move the leader
        self.all_turtles[0].forward(XDIST)
        # change the coordinates of the remaining turtles accordingly.
        for turtles in range(0, len(self.x_cor_turtles)):
            self.all_turtles[turtles + 1].goto(self.x_cor_turtles[turtles], self.y_cor_turtles[turtles])

        return self.check_wall()

    def add_turtl(self):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        self.all_turtles.append(new_turtle)

    def leader(self):
        coord_leader = [self.x_cor_turtles[0], self.y_cor_turtles[0]]
        return coord_leader

    def check_wall(self):
        # check for wall
        if self.all_turtles[0].xcor() >= 290:
            self.is_on = False
            g_o = Turtle()
            g_o.color("white")
            g_o.hideturtle()
            g_o.write("Game Over", align="center", font=("Arial", 20, "normal"))
        elif self.all_turtles[0].xcor() <= -290:
            self.is_on = False
            g_o = Turtle()
            g_o.color("white")
            g_o.hideturtle()
            g_o.write("Game Over", align="center", font=("Arial", 20, "normal"))
        elif self.all_turtles[0].ycor() <= -290:
            self.is_on = False
            g_o = Turtle()
            g_o.color("white")
            g_o.hideturtle()
            g_o.write("Game Over", align="center", font=("Arial", 20, "normal"))
        elif self.all_turtles[0].ycor() >= 290:
            self.is_on = False
            g_o = Turtle()
            g_o.color("white")
            g_o.hideturtle()
            g_o.write("Game Over", align="center", font=("Arial", 20, "normal"))
        else:
            for pos in range(1, len(self.x_cor_turtles)):
                if self.all_turtles[0].xcor() - 10 <= self.all_turtles[pos].xcor() <= self.all_turtles[
                    0].xcor() + 10 and self.all_turtles[0].ycor() - 10 <= \
                        self.all_turtles[pos].ycor() <= self.all_turtles[0].ycor() + 10:
                    self.is_on = False
                    g_o = Turtle()
                    g_o.color("white")
                    g_o.hideturtle()
                    g_o.write("Game Over", align="center", font=("Arial", 20, "normal"))
        return self.is_on

    def up(self):
        self.all_turtles[0].setheading(90)

    def down(self):
        self.all_turtles[0].setheading(270)

    def left(self):
        self.all_turtles[0].setheading(180)

    def right(self):
        self.all_turtles[0].setheading(0)
