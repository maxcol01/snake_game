from turtle import Turtle
from random import randint
from snake import Snake

snake = Snake()


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.y_cor_food = 0
        self.x_cor_food = 0
        self.coord_food = []
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def initialize_food(self):
        self.x_cor_food = randint(-280, 280)
        self.y_cor_food = randint(-280, 280)
        self.goto(self.x_cor_food, self.y_cor_food)

    def coord_food_to_catch(self):
        cor = [self.x_cor_food, self.y_cor_food]
        return cor

    def collision(self, c_leader, c_food):
        if c_leader[0] - 15 <= c_food[0] <= c_leader[0] + 15 and c_leader[1] - 15 <= c_food[1] <= c_leader[1] + 15:
            return True
